"""
Course: CSE 251
Lesson Week: 09
File: team2.py
Purpose: team activity - Dining philosophers problem
Problem statement
Five silent philosophers sit at a round table with bowls of spaghetti. Forks
are placed between each pair of adjacent philosophers.
Each philosopher must alternately think and eat. However, a philosopher can
only eat spaghetti when they have both left and right forks. Each fork can be
held by only one philosopher and so a philosopher can use the fork only if it
is not being used by another philosopher. After an individual philosopher
finishes eating, they need to put down both forks so that the forks become
available to others. A philosopher can only take the fork on their right or
the one on their left as they become available and they cannot start eating
before getting both forks.  When a philosopher is finished eating, they think 
for a little while.
Eating is not limited by the remaining amounts of spaghetti or stomach space;
an infinite supply and an infinite demand are assumed.
The problem is how to design a discipline of behavior (a concurrent algorithm)
such that no philosopher will starve
Instructions:
        **************************************************
        ** DO NOT search for a solution on the Internet **
        ** your goal is not to copy a solution, but to  **
        ** work out this problem.                       **
        **************************************************
- This is the same problem as last team activity.  However, you will implement a waiter.  
  When a philosopher wants to eat, it will ask the waiter if it can.  If the waiter 
  indicates that a philosopher can eat, the philosopher will pick up each fork and eat.  
  There must not be a issue picking up the two forks since the waiter is in control of 
  the forks and when philosophers eat.  When a philosopher is finished eating, it will 
  informs the waiter that he/she is finished.  If the waiter indicates to a philosopher
  that they can not eat, the philosopher will wait between 1 to 3 seconds and try again.
- You have Locks and Semaphores that you can use.
- Remember that lock.acquire() has an argument called timeout.
- philosophers need to eat for 1 to 3 seconds when they get both forks.  
  When the number of philosophers has eaten MAX_MEALS times, stop the philosophers
  from trying to eat and any philosophers eating will put down their forks when finished.
- philosophers need to think for 1 to 3 seconds when they are finished eating.  
- When a philosopher is not eating, it will think for 3 to 5 seconds.
- You want as many philosophers to eat and think concurrently.
- Design your program to handle N philosophers and N forks after you get it working for 5.
- Use threads for this problem.
- When you get your program working, how to you prove that no philosopher will starve?
  (Just looking at output from print() statements is not enough)
- Are the philosophers each eating and thinking the same amount?
- Using lists for philosophers and forks will help you in this program.
  for example: philosophers[i] needs forks[i] and forks[i+1] to eat
"""

import time
import threading

PHILOSOPHERS = 5
MAX_MEALS = PHILOSOPHERS * 5

class Person(threading.Thread):
    # True while they are still eating
    running = True

    def __init__(self, index, forkOnLeft, forkOnRight, allAte):
        threading.Thread.__init__(self)
        self.index = index # which philosopher
        self.forkOnLeft = forkOnLeft # left fork
        self.forkOnRight = forkOnRight # right fork
        self.allAte = allAte # list of who ate

    def run(self):
        while(self.running):
            # print(f'{self.index=}')
            print ('Philosopher %s is hungry.' % self.index)
            self.sitting()

    def sitting(self):
        # if both the semaphores(forks) are free, then philosopher will eat
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while self.running:
            fork1.acquire() # locks fork
            locked = fork2.acquire(False) 
            if locked: # checks if the other fork is available
              break 
            fork1.release()
            fork1, fork2 = fork2, fork1
        else:
            return
        self.eat()
        #releases forks
        fork2.release()
        fork1.release()
 
    def eat(self):
        print ('Philosopher %s starts eating. ' % self.index)
        time.sleep(10)
        print ('Philosopher %s finishes eating and starts thinking.' % self.index)
        time.sleep(10)
        print ('Philosopher %s finishes thinking. ' % self.index)
        self.allAte.append(self.index)
        done = [0, 1, 2, 3, 4]
        result =  all(elem in self.allAte for elem in done)
        if result:
          print('Everyone Ate!')
          
          pil1 = self.allAte.count(0)
          pil2 = self.allAte.count(1)
          pil3 = self.allAte.count(2)
          pil4 = self.allAte.count(3)
          pil5 = self.allAte.count(4)
      
          print(f'Philospher 1 ate {pil1} meals')
          print(f'Philospher 2 ate {pil2} meals')
          print(f'Philospher 3 ate {pil3} meals')
          print(f'Philospher 4 ate {pil4} meals')
          print(f'Philospher 5 ate {pil5} meals')
          self.running = False
          return

def main():

    # creates semaphores for the forks
    forks = []
    for x in range(PHILOSOPHERS):
      t = threading.Semaphore()
      forks.append(t)
    allAte = []
    philosophers = []
    for x in range(5):
      p = Person(x, forks[x-1], forks[x], allAte)
      philosophers.append(p)
    
    
    Person.running = True
    for p in philosophers: 
      p.start()
    time.sleep(100)
    Person.running = False
 

if __name__ == "__main__":
    main()