"""
Course: CSE 251
Lesson Week: 05
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- See in I-Learn

"""

import threading
import queue
import requests
import json

# Include cse 251 common Python files
from cse251 import *

RETRIEVE_THREADS = 1        # Number of retrieve_threads
NO_MORE_VALUES = 'No more'  # Special value to indicate no more items in the queue

def retrieve_thread(q):  # TODO add arguments
    """ Process values from the data_queue """
    
    while True:

        url = q.get()
        if url == NO_MORE_VALUES:
            break
        else:
            response = requests.get(url)
    
            print(response.json)    
 
        # TODO process the value retrieved from the queue

        # TODO make Internet call to get characters name and log it
         



def file_reader(log, q): # TODO add arguments
    """ This thread reading the data file and places the values in the data_queue """

    # TODO Open the data file "urls.txt" and place items into a queue
    f = open('urls.txt', 'r')
    for line in f:
        q.put(line.strip())

    log.write('finished reading file')

    # TODO signal the retrieve threads one more time that there are "no more values"
    q.put(NO_MORE_VALUES)


def main():
    """ Main function """

    log = Log(show_terminal=True)

    # TODO create queue
    q = queue.Queue()
    # TODO create semaphore (if needed)

    # TODO create the threads. 1 filereader() and RETRIEVE_THREADS retrieve_thread()s
    # Pass any arguments to these thread need to do their job

    log.start_timer()                       

    # TODO Get them going - start the retrieve_threads first, then file_reader
    # retrieve_thread(q)
    retrieve_thread(q)
    file_reader(log, q)
    retrieve_thread(q)
    # TODO Wait for them to finish - The order doesn't matter

    log.stop_timer('Time to process all URLS')


if __name__ == '__main__':
    main()




