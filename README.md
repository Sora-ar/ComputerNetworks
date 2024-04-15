The Computer Networks and Distributed Computing course consists of three tasks that require the use of knowledge of threads. 
The work was done on Python.  
  
  
<h3>Task #1.
Create a simple program with 2 threads  </h3>
Write a code that contains a global variable - int data = 0 and two threads (one in a loop increments the variable by 1, the other thread decrements it by 1).
The 1st thread terminates if data == 1000,
the 2nd thread ends its work if data == -1000.
Which thread will finish its work first?
When one thread is stopped, the other one also stops.

<h3>Task #2.
Creating a program with 2 threads using mutexes  </h3>
Write a code that contains a list - list <int> and two threads. In one thread, the list contains numbers generated using a random number generator. In the other thread, these numbers are displayed on the screen.
Organize the work of the threads so that the interaction with the list is correct. Use mutexes to organize the work of threads.

<h3>Task # 3
Creating the program Philosophers  </h3>
Develop a program that emulates the activities of the Philosophers, if you know that:  
a) There are 5 philosophers, 5 plates, 5 forks  
b) A philosopher can be in two states:  
   1. Thinking  
   2. Eating
      
c) In order to eat, two forks are needed  
d) The philosopher can eat for some time (a random number) before he starts thinking. If the philosopher has two free forks, he eats.  
e) At the beginning, all Philosophers are thinking.  
The program displays the current state of the Philosophers.
