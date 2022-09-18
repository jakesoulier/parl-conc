# TODO import the appropriate threading and thread modules
from cse251 import Log
import threading

# TODO create a global counter
count_global = 0
# TODO create a summing function that to target using the threading module.
def count(number):
    global count_global
    for x in range(number):
        count_global += 1
        print(f'{x}')
# TODO create a class that extends the Thread class (make sure you use a constructor and have a run function)
class Thread():
    def __init__(self):
        pass

    def run(self):
        print('running thread')
        

# Note: don't change the name of this function or the unit test won't work
def create_threads(number, log):
    ''' number = the range to sum over, so if numbers equals 10, 
        then the sum will be 1 + 2 + ... + 9 + 10 = 45 
    '''
    log.write(f'number={number}')

    t1 = threading.Thread(target=thread_function)
    t1.start() 
    # Two ways to create a thread:
    # 1) Create a class that extends Thread and then instantiate that class
    # 2) Instantiate Thread and give it a target and arguments

    # LEAVE THIS so that your code can be tested against the unit test
    # (you can change the name of these variables)
    return sum_numbers_object.sum or t1, sum_global

# Leave this so that you can run your code without needed to run the unit test.
# Once you believe it is working, run the unit test (challenge01_test.py) to 
# verify that it works against more numbers than 10.
if __name__ == '__main__':
    log = Log(show_terminal=True)
    create_threads(10, log)
