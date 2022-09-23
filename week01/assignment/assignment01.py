# TODO import the appropriate threading and thread modules
from cse251 import Log
import threading

# TODO create a global counter
count_global = 0
# TODO create a summing function that to target using the threading module.
# def count(number):
#     global count_global
#     for x in range(number):
#         count_global += 1
        # print(f'x={x}')
# TODO create a class that extends the Thread class (make sure you use a constructor and have a run function)
class MyThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        # log.write(f'number={number}')
        # print(f'{self.name} is being made')
        self.sum = 0
        # count_global = 0
        self.number = number
        self.local_count = 0

    def run(self):
        # print(f'{self.name} start running')
        # count(self.number)
        for x in range(self.number):
            # self.sum += 1
            self.print_message()
        print(f'{self.name}, final sum using run={self.sum}')
        # print(f'{self.name} end run') 

    def print_message(self):
        # self.count_local += 1
        global count_global
        
        self.sum = count_global + self.sum
        count_global += 1
        self.local_count += 1
        print(f'{self.name}, x={self.local_count}, sum={self.sum}')

# Note: don't change the name of this function or the unit test won't work
def create_threads(number, log):
    ''' number = the range to sum over, so if numbers equals 10, 
        then the sum will be 1 + 2 + ... + 9 + 10 = 45 
    '''
    
    global count_global
    count_global = 0
    print(f'number={number}')
    t1 = MyThread(number)
    t1.start()
    t1.join()
    
    # log.write(f'number={number}')
    
    t2 = MyThread(number)
    t2.start()
    t2.join()
    
    # log.write(f'number={number}')
    # t3 = MyThread(17)
    # t3.start()
    # t3.join()
    # print(f'Return values from create_threads: actual_from_class={number}, actual_from_thread_mod={t1.sum}')
    
    # threading.Thread(target=count, args=(10,))
    # t1 = threading.Thread(target=thread_function)
    # t1.start() 
    # Two ways to create a thread:
    # 1) Create a class that extends Thread and then instantiate that class
    # 2) Instantiate Thread and give it a target and arguments

    # LEAVE THIS so that your code can be tested against the unit test
    # (you can change the name of these variables)
    return t1.sum, t1.sum


# Leave this so that you can run your code without needed to run the unit test.
# Once you believe it is working, run the unit test (challenge01_test.py) to 
# verify that it works against more numbers than 10.
if __name__ == '__main__':
    log = Log(show_terminal=True)
    create_threads(10, log)
    # print('end')
