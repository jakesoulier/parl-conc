"""
Course: CSE 251
Lesson Week: 10
File: Assignment.py
"""

import time
import random
import multiprocessing as mp

# number of cleaning staff and hotel guests
CLEANING_STAFF = 2
HOTEL_GUESTS = 5

# Run program for this number of seconds
TIME = 10

STARTING_PARTY_MESSAGE =  'Turning on the lights for the party vvvvvvvvvvvvvv'
STOPPING_PARTY_MESSAGE  = 'Turning off the lights  ^^^^^^^^^^^^^^^^^^^^^^^^^^'

STARTING_CLEANING_MESSAGE =  'Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
STOPPING_CLEANING_MESSAGE  = 'Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'

def cleaner_waiting():
    time.sleep(random.uniform(0, 2))

def cleaner_cleaning(id):
    print(f'Cleaner {id}')
    time.sleep(random.uniform(0, 2))

def guest_waiting():
    time.sleep(random.uniform(0, 2))

def guest_partying(id):
    print(f'Guest {id}')
    time.sleep(random.uniform(0, 1))

def cleaner(count, room, lock, start_time):
    """
    do the following for TIME seconds
        cleaner will wait to try to clean the room (cleaner_waiting())
        get access to the room
        display message STARTING_CLEANING_MESSAGE
        Take some time cleaning (cleaner_cleaning())
        display message STOPPING_CLEANING_MESSAGE
    """
    end_time = start_time + TIME
    # print(end_time)
    while time.time() < end_time:
        cleaner_waiting()
        # print(room.value)
        if room.value == 0:
            lock.acquire()
            print(STARTING_CLEANING_MESSAGE)
            room.value += 1
            count.value += 1
            cleaner_cleaning(1)
            print(STOPPING_CLEANING_MESSAGE)
            room.value -= 1
            lock.release()

def guest(party_count, room,lock, start_time):
    """
    do the following for TIME seconds
        guest will wait to try to get , access to the room (guest_waiting())
        get access to the room
        display message STARTING_PARTY_MESSAGE if this guest is the first one in the room
        Take some time partying (guest_partying())
        display message STOPPING_PARTY_MESSAGE if the guest is the last one leaving in the room
    """
    end_time = start_time + TIME
    while time.time() < end_time:
        guest_waiting()
        lock.acquire()
        # room.value += 1
        party_count.value += 1
        # while room.value > 0:
        print(STARTING_PARTY_MESSAGE)
        guest_partying(1)
        # room.value += 1
        print(STOPPING_PARTY_MESSAGE)
        lock.release()

def main():
    # Start time of the running of the program. 
    start_time = time.time()

    # TODO - add any variables, data structures, processes you need
    # TODO - add any arguments to cleaner() and guest() that you need

    # manager = mp.Manager()
    # room = manager.dict()
    # room[0]
    lock = mp.Lock()

    cleaned_count = mp.Value('d', 0)
    party_count = mp.Value('d', 0)
    room = mp.Value('d', 0)
    clean = mp.Process(target=cleaner, args=(cleaned_count, room, lock, start_time))
    party = mp.Process(target=guest, args=(party_count, room, lock, start_time))

    clean.start()
    party.start()
    clean.join()
    party.join()
    # Results
    print(f'Room was cleaned {cleaned_count.value} times, there were {party_count.value} parties')


if __name__ == '__main__':
    main()

