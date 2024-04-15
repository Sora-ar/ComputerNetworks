import threading
import random
import time


class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f"{self.name} is thinking")
        time.sleep(random.uniform(1, 3))

    def eat(self):
        print(f"{self.name} is hungry")
        with self.left_fork:
            with self.right_fork:
                print(f"{self.name} starts eating")
                time.sleep(random.uniform(1, 3))
                print(f"{self.name} finished eating")


if __name__ == "__main__":
    num_philosophers = 5
    forks = [threading.Lock() for _ in range(num_philosophers)]
    philosophers = [Philosopher(f"Philosopher {i + 1}", forks[i], forks[(i + 1) % num_philosophers])
                    for i in range(num_philosophers)]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

# In this program, each philosopher is a separate stream.
# Each thread tries to grab two forks to start eating.
# If the forks are not available, the philosopher goes into a waiting state.
# When the forks become available, the philosopher starts eating.
# After eating, he returns the forks and starts thinking.
