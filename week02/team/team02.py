"""
Course: CSE 251
Lesson Week: 02 - Team Acvitiy
File: team.py
Author: Brother Comeau

Purpose: Find prime numbers

Instructions:

- Don't include any other Python packages or modules
- Review team acvitiy details in I-Learn

"""

from datetime import datetime, timedelta
import threading


# Include cse 251 common Python files
from cse251 import *

# Global variable for counting the number of primes found
prime_count = 0
numbers_processed = 0

def is_prime(n: int):
    global numbers_processed
    numbers_processed += 1

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

def prime_sum(begin, end):
        global prime_count
        for x in range(begin, end):
            if is_prime(x):
                prime_count += 1


if __name__ == '__main__':
    log = Log(show_terminal=True)
    log.start_timer()

    # TODO 1) Get this program running
    # TODO 2) move the following for loop into 1 thread
    # TODO 3) change the program to divide the for loop into 10 threads

    start = 10000000000
    range_count = 100000
    increment = 10000
    # for i in range(start, range_count):
    # for x in range(start, start+range_count):
    
    
                
    updated_start = start
    for x in range(10):
        t = threading.Thread(target=prime_sum, args=(updated_start, updated_start + increment))
        updated_start += 10000
        t.start()
        t.join()
    
    
    # for x in range(4):
        
        
        
        
        
    #     if is_prime(i):
    #         prime_count += 1
    #         print(i, end=', ', flush=True)
    # print(flush=True)
    

    # Should find 4306 primes
    log.write(f'Numbers processed = {numbers_processed}')
    log.write(f'Primes found      = {prime_count}')
    log.stop_timer('Total time')


