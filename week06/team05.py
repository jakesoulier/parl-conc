"""
Course: CSE 251
Lesson Week: 05
File: team.py
Author: Brother Comeau

Purpose: Check for prime values

Instructions:

- You can't use thread pools or process pools
- Follow the graph in I-Learn 
- Start with PRIME_PROCESS_COUNT = 1, then once it works, increase it

"""
import time
import threading
import multiprocessing as mp
import random

#Include cse 251 common Python files
from cse251 import *

PRIME_PROCESS_COUNT = 1

def is_prime(n: int):
    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# TODO create read_thread function
def read_thread(queue):
    """Reads data.txt file and adds each number or line to the queue"""
    with open('data.txt', 'r') as f:
        for line in f:
            # print(f'Line added: {line}')
            queue.put(int(line.strip()))
        print('---Put data in queue---')
    queue.put(None)
    queue.put(None)
    queue.put(None)

# TODO create prime_process function
def prime_process(queue, prime_list):
    """ Reads from queue and uses the `is_prime`
    method on the value. If `is_prime` returns True,
    it is placed on the `prime_list`
    """
    while True:
        num = queue.get()
        # print(f'num before evaluation: {num}')
        if num == None:
            break
        
        if is_prime(num):
            # print(f"{num} is prime.")
            prime_list.append(num)


def create_data_txt(filename):
    with open(filename, 'r') as f:
        for _ in range(1000):
            f.write(str(random.randint(10000000000, 100000000000000)) + '\n')


def main():
    """ Main function """

    # filename = 'data.txt'

    # Once the data file is created, you can comment out this line
    # create_data_txt(filename)

    log = Log(show_terminal=True)
    log.start_timer()

    # TODO Create shared data structures
    q = mp.Queue()
    list_primes = mp.Manager().list([])
    
    # TODO create reading thread
    thread = threading.Thread(target=read_thread, args=(q,))

    # TODO create prime processes
    p1 = mp.Process(target = prime_process,args = (q, list_primes))
    p2 = mp.Process(target = prime_process,args = (q, list_primes))
    p3 = mp.Process(target = prime_process,args = (q, list_primes))
    
    # TODO Start them all
    thread.start()
    p1.start()
    p2.start()
    p3.start()
    
    # TODO wait for them to complete
    thread.join()
    p1.join()
    p2.join()
    p3.join()

    log.stop_timer(f'All primes have been found using {PRIME_PROCESS_COUNT} processes')

    # display the list of primes
    print(f'There are {len(list_primes)} found:')
    for prime in list_primes:
        print(prime)


if __name__ == '__main__':
    main()

