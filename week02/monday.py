# '''pass by reference'''

# def assign_new_value(a):
#     print(f'INSIDE FUNCTION: before id ={id(a)}')
#     a = 10
#     print(f'INSIDE FUNCTION:  after id ={id(a)}')
    
# my_int = 20
# assign_new_value(my_int)
# print(f'OUTSIDE FUNCTION:  after id ={id(my_int)}')
# print(my_int)
from msvcrt import kbhit
import threading
from time import sleep
from unittest.util import _count_diff_all_purpose
count = 0

def increase(value: int):
    global count
    local_count = count
    print(f'{threading.current_thread().name} - BEFORE: global counter id={id(count)}\n', end="")
    print(f'{threading.current_thread().name} - BEFORE: local counter id={id(local_count)}\n', end="")
    
    local_count += value
    # sleep(0.1)
    
    
    print(f'{threading.current_thread().name} - AFTER: global counter id={id(count)}\n', end="")
    print(f'{threading.current_thread().name} - AFTER: local counter id={id(local_count)}\n', end="")
    
    lock.acquire()
    count = local_count
    lock.release()
    print(f'{threading.current_thread().name} - counter={count}\n', end="")

lock = threading.Lock()

t1 = threading.Thread(target=increase, args=(10,))
t2 = threading.Thread(target=increase, args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()

