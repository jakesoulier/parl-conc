"""
Course: CSE 251
Lesson Week: 09
File: assingnment.py
Author: Jake Soulier
Purpose: Process Task Files

Instructions:  See I-Learn

TODO

I tested many different pool sizes and compared how
fast they ran the tasks. I found that even if I ran
the same number of pools, I would get a different 
completion time so I made sure to test each pool   
size multiple times. I found that the main drop was
when I set the pool size to 10. This decreased the 
average completion time down to around 10 seconds,
while anything below 10 was getting closer to 20 seconds
and anything over 10 pools was remaining around the same time.

"""

from datetime import datetime, timedelta
import requests
import multiprocessing as mp
from matplotlib.pylab import plt
import numpy as np
import glob
import math 

# Include cse 251 common Python files - Dont change
from cse251 import *

TYPE_PRIME  = 'prime'
TYPE_WORD   = 'word'
TYPE_UPPER  = 'upper'
TYPE_SUM    = 'sum'
TYPE_NAME   = 'name'

# Global lists to collect the task results
result_primes = []
result_words = []
result_upper = []
result_sums = []
result_names = []

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
 
def task_prime(value):
    """
    implement logic to check if number is prime or not
    """

    if is_prime(value):
        # print(f'{value} is prime')
        # result_primes.append(f'{value} is prime')
        return (f'{value} is prime')
    else:
        # print(f'{value} is not prime')
        return (f'{value} is not prime')

def task_word(word):
    """
    Open "words.txt" file"
    checks if word is in file
    """
    with open('words.txt', 'r') as f:
        contents = f.read()
        if word in contents:
            # result_words.append(f'{word} is in the text file')
            return (f'{word} is in the text file')

def task_upper(text):
    """
    converts text to all uppercase
    """
    return (text.upper())

def task_sum(start_value, end_value):
    """
    Add the two values, return there sum
    """
    total = start_value + end_value
    return (f'sum of {start_value:,} to {end_value:,} = {total:,}')

def task_name(url):
    """
    use given url to retrieve and review information
    get the name and return it
    """
    response = requests.get(url)
    responseJson = response.json()
    if responseJson != None: 
        name = responseJson['name']
        return (f'{url} has name {name}')
    else:
        # result_names.append(f'{url} had an error receiving the information')
        return (f'{url} had an error receiving the information')

"""
callback for each apply_sync task function
returns a value by appending it to a global list
"""
def log_primes(result):
    result_primes.append(result)
def log_words(result):
    result_words.append(result)
def log_upper(result):
    result_upper.append(result)
def log_sum(result):
    result_sums.append(result)
def log_names(result):
    result_names.append(result)

def main():
    log = Log(show_terminal=True)
    log.start_timer()

    # TODO Create process pools
    pool = mp.Pool(10)
    count = 0
    task_files = glob.glob("*.task")
    for filename in task_files:
        task = load_json_file(filename)
        count += 1
        task_type = task['task']
        if task_type == TYPE_PRIME: # if 'task': "" = 'prime'
            pool.apply_async(task_prime, args=(task['value'],), callback=log_primes)
        elif task_type == TYPE_WORD: # if 'task': "" = 'word'
            pool.apply_async(task_word, args=(task['word'],), callback=log_words)
        elif task_type == TYPE_UPPER: # if 'task': "" = 'upper'
            pool.apply_async(task_upper, args=(task['text'],), callback=log_upper)
        elif task_type == TYPE_SUM: # if 'task': "" = 'sum'
            pool.apply_async(task_sum, args=(task['start'], task['end']), callback=log_sum)
        elif task_type == TYPE_NAME: # if 'task': "" = 'name'
            pool.apply_async(task_name, args=(task['url'],), callback=log_names)
        else:
            log.write(f'Error: unknown task type {task_type}')

    # TODO start and wait pools
    pool.close()
    pool.join()

    # Do not change the following code (to the end of the main function)
    def log_list(lst, log):
        for item in lst:
            log.write(item)
        log.write(' ')
    
    log.write('-' * 80)
    log.write(f'Primes: {len(result_primes)}')
    log_list(result_primes, log)

    log.write('-' * 80)
    log.write(f'Words: {len(result_words)}')
    log_list(result_words, log)

    log.write('-' * 80)
    log.write(f'Uppercase: {len(result_upper)}')
    log_list(result_upper, log)

    log.write('-' * 80)
    log.write(f'Sums: {len(result_sums)}')
    log_list(result_sums, log)

    log.write('-' * 80)
    log.write(f'Names: {len(result_names)}')
    log_list(result_names, log)

    log.write(f'Number of Primes tasks: {len(result_primes)}')
    log.write(f'Number of Words tasks: {len(result_words)}')
    log.write(f'Number of Uppercase tasks: {len(result_upper)}')
    log.write(f'Number of Sums tasks: {len(result_sums)}')
    log.write(f'Number of Names tasks: {len(result_names)}')
    log.stop_timer(f'Finished processes {count} tasks')

if __name__ == '__main__':
    main()
