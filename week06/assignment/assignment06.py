"""
Course: CSE 251
Lesson Week: 06
File: assignment06.py
Author: Jake Soulier

Purpose: Assignment 06 - Factories and Dealers

Instructions:

- Read the comments in the following code.  
- Implement your code where the TODO comments are found.
- No global variables, all data must be passed to the objects.
- Only the included/imported packages are allowed.  
- Thread/process pools are not allowed
- You are not allowed to use the normal Python Queue object.  You must use Queue251.
- the shared queue between the threads that are used to hold the Car objects
  can not be greater than MAX_QUEUE_SIZE

"""

from datetime import datetime, timedelta
import time
import threading
import random
import multiprocessing as mp

# Include cse 251 common Python files
from cse251 import *

# Global Consts
MAX_QUEUE_SIZE = 10
SLEEP_REDUCE_FACTOR = 50

# NO GLOBAL VARIABLES!

class Car():
    """ This is the Car class that will be created by the factories """

    # Class Variables
    car_makes = ('Ford', 'Chevrolet', 'Dodge', 'Fiat', 'Volvo', 'Infiniti', 'Jeep', 'Subaru', 
                'Buick', 'Volkswagen', 'Chrysler', 'Smart', 'Nissan', 'Toyota', 'Lexus', 
                'Mitsubishi', 'Mazda', 'Hyundai', 'Kia', 'Acura', 'Honda')

    car_models = ('A1', 'M1', 'XOX', 'XL', 'XLS', 'XLE' ,'Super' ,'Tall' ,'Flat', 'Middle', 'Round',
                'A2', 'M1X', 'SE', 'SXE', 'MM', 'Charger', 'Grand', 'Viper', 'F150', 'Town', 'Ranger',
                'G35', 'Titan', 'M5', 'GX', 'Sport', 'RX')

    car_years = [i for i in range(1990, datetime.now().year)]

    def __init__(self):
        # Make a random car
        self.model = random.choice(Car.car_models)
        self.make = random.choice(Car.car_makes)
        self.year = random.choice(Car.car_years)

        # Sleep a little.  Last statement in this for loop - don't change
        time.sleep(random.random() / (SLEEP_REDUCE_FACTOR))

        # Display the car that has was just created in the terminal
        self.display()
           
    def display(self):
        print(f'{self.make} {self.model}, {self.year}')


class Queue251():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []
        self.max_size = 0

    def get_max_size(self):
        return self.max_size
        
    def put(self, item):
        self.items.append(item)
        if len(self.items) > self.max_size:
            self.max_size = len(self.items)

    def get(self):
        return self.items.pop(0)


class Factory(threading.Thread):
    """ This is a factory.  It will create cars and place them on the car queue """
    def __init__(self, queue, sem_empty: threading.Semaphore, sem_full: threading.Semaphore, lock, barrier: threading.Barrier, factory_stats, factory_count, dealer_count, total_factory_count):
            super(Factory, self).__init__()
            self.cars_to_produce = random.randint(200, 300)     # Don't change
            self.queue = queue
            self.sem_empty = sem_empty
            self.sem_full = sem_full
            self.lock = lock
            self.barrier = barrier
            self.stats = factory_stats
            self.count = factory_count
            self.dealer_count = dealer_count
            self.total_fact_count = total_factory_count
    def run(self):
        # TODO produce the cars, the send them to the dealerships
        for i in range(self.cars_to_produce):
            self.sem_full.acquire()
            car = Car() # get a car
            with self.lock:
                self.queue.put(car) # place car in queue
            self.stats[self.count-1] += 1 # add count of added cars in factory
            self.sem_empty.release()
        # TODO wait until all of the factories are finished producing cars
        self.barrier.wait()
        # select only one factory
        if self.count == 0:
            # adds 'None' only to how many dealerships are available
            for x in range(self.dealer_count):
                self.queue.put(None) # add None to end of queue
                self.sem_empty.release()
            # signals dealerships one more time
            self.sem_empty.release()
            
class Dealer(threading.Thread):
    """ This is a dealer that receives cars """

    def __init__(self, queue, sem_empty: threading.Semaphore, sem_full: threading.Semaphore, lock, barrier: threading.Barrier, dealer_stats, dealer_count):
        super(Dealer, self).__init__()
        self.queue = queue
        self.sem_empty = sem_empty
        self.sem_full = sem_full
        self.lock = lock
        self.stats = dealer_stats
        self.barrier = barrier
        self.count = dealer_count

    def run(self):
        while True:
            # TODO handle a car
            self.sem_empty.acquire()
            with self.lock:
                car = self.queue.get()
                if car == None:
                    break
                self.stats[self.count-1] += 1 # counts each car added to dealership

            self.sem_full.release()
            
            # Sleep a little - don't change.  This is the last line of the loop
            time.sleep(random.random() / (SLEEP_REDUCE_FACTOR + 0))



def run_production(factory_count, dealer_count):
    """ This function will do a production run with the number of
        factories and dealerships passed in as arguments.
    """

    # TODO Create semaphore(s)
    sem_full = threading.Semaphore(MAX_QUEUE_SIZE)
    sem_empty = threading.Semaphore(0)
    # TODO Create queue
    q = Queue251()
    # TODO Create lock(s)
    lock = threading.Lock()
    # TODO Create barrier(s)
    factory_barrier = mp.Barrier(factory_count)  
    dealer_barrier = mp.Barrier(dealer_count - 1)   
    # This is used to track the number of cars receives by each dealer
    dealer_stats = list([0] * dealer_count)
    # This counts the numbers of cars produced by each factory
    factory_stats = [0]

    # TODO create your factories, each factory will create CARS_TO_CREATE_PER_FACTORY
    factory = [Factory(q, sem_empty, sem_full, lock, factory_barrier, factory_stats, i, dealer_count, factory_count) for i in range(factory_count)]
    # TODO create your dealerships
    dealer = [Dealer(q, sem_empty, sem_full, lock, dealer_barrier, dealer_stats, i) for i in range(dealer_count)]
    log.start_timer()

    # TODO Start all dealerships
    for i in range(dealer_count):
        dealer[i].start()

    time.sleep(1)   # make sure all dealers have time to start

    # TODO Start all factories
    for i in range(factory_count):
        factory[i].start()
    # TODO Wait for factories and dealerships to complete
    
    for i in range(factory_count):
        factory[i].join()
    for i in range(dealer_count):
        dealer[i].join()
    run_time = log.stop_timer(f'{sum(dealer_stats)} cars have been created')


    
    # This function must return the following - Don't change!
    # factory_stats: is a list of the number of cars produced by each factory.
    #                collect this information after the factories are finished. 
    return (run_time, q.get_max_size(), dealer_stats, factory_stats)


def main(log):
    """ Main function - DO NOT CHANGE! """

    runs = [(1, 1), (1, 2), (2, 1), (2, 2), (2, 5), (5, 2), (10, 10)]
    for factories, dealerships in runs:
        print(f'factories: {factories}')
        print(f'dealers: {dealerships}')
        run_time, max_queue_size, dealer_stats, factory_stats = run_production(factories, dealerships)

        log.write(f'Factories      : {factories}')
        log.write(f'Dealerships    : {dealerships}')
        log.write(f'Run Time       : {run_time:.4f}')
        log.write(f'Max queue size : {max_queue_size}')
        log.write(f'Factor Stats   : {factory_stats}')
        log.write(f'Dealer Stats   : {dealer_stats}')
        log.write('')

        # The number of cars produces needs to match the cars sold
        assert sum(dealer_stats) == sum(factory_stats)


if __name__ == '__main__':

    log = Log(show_terminal=True)
    main(log)


