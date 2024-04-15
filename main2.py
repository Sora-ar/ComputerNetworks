import threading
import random
import time
import logging


# Налаштування логування
def get_log(log_level):
    local_logger = logging.getLogger("user_data")
    local_logger.setLevel(log_level)

    file_handler = logging.FileHandler('app2.log')
    file_handler.setLevel(log_level)

    local_logger.addHandler(file_handler)

    return local_logger


# Функція для додавання чисел до списку
def thread_func1():
    global x
    while True:
        num = random.randint(1, 100)
        mutex.acquire()
        x.append(num)
        logger.debug("Added number %d to the list", num)
        logger.debug("Current list: %s", x)
        mutex.release()
        time.sleep(1)


# Функція для видалення чисел зі списку
def thread_func2():
    global x
    while True:
        mutex.acquire()
        if x:
            num = x.pop()
            logger.debug("Number %d is removed from the list", num)
            logger.debug("Current list: %s", x)
        else:
            logger.debug("List is empty")
        mutex.release()
        time.sleep(2)


# Глобальний список та м'ютекс для забезпечення потокобезпеки
x = []
mutex = threading.Lock()

# Отримуємо об'єкта логгера
logger = get_log(logging.DEBUG)

# Створюємо потоки
thread1 = threading.Thread(target=thread_func1)
thread2 = threading.Thread(target=thread_func2)

# Запускаємо потоки
thread1.start()
thread2.start()

# Очікуємо завершення обох потоків (не досягнеся, так як вони безкінечні)
thread1.join()
thread2.join()
