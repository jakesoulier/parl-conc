"""
Course: CSE 251
Lesson Week: 05
File: assignment.py
Author: <Your name>

Purpose: Assignment 05 - Factory and Dealership

Instructions:

- See I-Learn

"""

from concurrent.futures import thread
from multiprocessing import Semaphore
from os import stat
import time
import threading
import random

# Include cse 251 common Python files
from cse251 import *

# Global Consts - Do not change
CARS_TO_PRODUCE = 500 # 500
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

        # Display the car that has just be created in the terminal
        self.display()
           
    def display(self):
        print(f'{self.make} {self.model}, {self.year}')


class Queue251():
    """ This is the queue object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

class Factory(threading.Thread):
    """ This is a factory.  It will create cars and place them on the car queue """
    def __init__(self, car_count, queue, sem_empty: threading.Semaphore, sem_full: threading.Semaphore, lock):
        super(Factory, self).__init__()
        
        self.car_count = car_count
        self.queue = queue
        self.sem_empty = sem_empty
        self.sem_full = sem_full
        self.lock = lock
    # def __init__(self, queue_stats,q,  fact_com, deal_com):
    #     # TODO, you need to add arguments that will pass all of data that 1 factory needs
    #     # to create cars and to place them in a queue.
    #     # self.car = []
    #     self.q = q
    #     self.queue_stats = queue_stats
    #     self.fact_com = fact_com
    #     self.deal_com = deal_com
    #     self.car = Car()
        
    def run(self):
        for i in range(self.car_count):
            self.sem_full.acquire()
            car = Car()
            with self.lock:
                self.queue.put(car)
            self.sem_empty.release()
            
        self.sem_full.acquire()
        
        self.queue.put(None)
        
        self.sem_empty.release()
        print('>>>>>>> factory ends')
  

        # signal the dealer that there there are not more cars
        # self.q.put('DONE')

class Dealer(threading.Thread):
    def __init__(self, queue, sem_empty: threading.Semaphore, sem_full: threading.Semaphore, stats, lock):
        super(Dealer, self).__init__()
        self.queue = queue
        self.sem_empty = sem_empty
        self.sem_full = sem_full
        self.stats = stats
        self.lock = lock
    """ This is a dealer that receives cars """

    # def __init__(self, q, queue_stats, fact_com, deal_com, thread_id):
    #     # TODO, you need to add arguments that pass all of data that 1 Dealer needs
    #     # to sell a car
    #     self.q = queue
    #     self.queue_stats = queue_stats
    #     self.fact_com = fact_com
    #     self.deal_com = deal_com
    #     self.thread_id = thread_id
    #     # self.sold_cars = []

    def run(self):
        while True:
            self.sem_empty.acquire()
            with self.lock:
                car = self.queue.get()
                if car == None:
                    break
                self.stats[self.queue.size()] += 1
            self.sem_full.release()
            
            # self.fact_com.acquire()
            # # self.deal_com.acquire()
            # # TODO Add your code here
            # # print(queue_stats)
            # self.queue_stats[self.thread_id] += 1
            # print(f'queue stats: {self.queue_stats[self.thread_id]}')
            # eva_car = self.q.get()
            
            # if eva_car == 'DONE':
            #     break
            # else:
            #     self.q.put(eva_car)
            #     # self.sold_cars.append(eva_car)
            # """
            # take the car from the queue
            # signal the factory that there is an empty slot in the queue
            # """
            # print(f'Just sold: {eva_car}')
            # self.deal_com.release()
            # self.fact_com.release()
            # Sleep a little after selling a car
            # Last statement in this for loop - don't change
            time.sleep(random.random() / (SLEEP_REDUCE_FACTOR))

def main():
    log = Log(show_terminal=True)

    # TODO Create semaphore(s)
    # fact_com = threading.Semaphore
    # deal_com = threading.Semaphore
    # TODO Create queue251 
    car_queue = Queue251()
    
    sem_full = threading.Semaphore(MAX_QUEUE_SIZE)
    
    sem_empty = threading.Semaphore(0)
    # TODO Create lock(s) ?
    # lock = threading.Lock()

    # This tracks the length of the car queue during receiving cars by the dealership
    # i.e., update this list each time the dealer receives a car
    stats = [0] * MAX_QUEUE_SIZE

    lock = threading.Lock()
    
    # TODO create your one factory
    # factory = threading.Thread(target=Factory, args=(CARS_TO_PRODUCE, car_queue, sem_empty, sem_full, lock,))
    # dealer = threading.Thread(target=Dealer, args=(car_queue, sem_empty, sem_full, stats, lock,))
    # factory = Factory(CARS_TO_PRODUCE, car_queue, sem_empty, sem_full, lock)
    # dealer = Dealer(car_queue, sem_empty, sem_full, stats, lock)
    # factory = [threading.Thread(target=Factory, args=(q, queue_stats, fact_com, deal_com)) for i in range(CARS_TO_PRODUCE)]
    # TODO create your one dealership
    # deal = Dealer()
    # deal = threading.Thread(target=Dealer, args=(q, queue_stats, fact_com, deal_com))
    # deal = [threading.Thread(target=Dealer, args=(q, queue_stats, fact_com, deal_com, i)) for i in range(CARS_TO_PRODUCE)]
    log.start_timer()

    dealer.start()
    factory.start()
    
    factory.join()
    dealer.join()
    # TODO Start factory and dealership
    # fact.run(q, communication)
    # fact.start()
    # deal.start()
    # for i in range(CARS_TO_PRODUCE):
    #     fact[i].start()
    #     deal[i].start() 
    # fact.join()                 
    # deal.join()
    # for i in range(CARS_TO_PRODUCE):
    #     fact[i].join()
    #     deal[i].join()
    # print(f'Queue stats: {queue_stats}')
    # deal.run(q, queue_stats, communication)
    # TODO Wait for factory and dealership to complete

    log.stop_timer(f'All {sum(stats)} have been created')

    xaxis = [i for i in range(1, MAX_QUEUE_SIZE + 1)]
    plot = Plots()
    plot.bar(xaxis, stats, title=f'{sum(stats)} Produced: Count VS Queue Size', x_label='Queue Size', y_label='Count')

if __name__ == '__main__':
    main()
