
# import threading
 
# class DiningPhilosophers:
#     def __init__(self):
#         # List of semaphores, one for each fork
#         self.forks = [threading.Semaphore(1) for _ in range(5)]
 
#     # call the functions directly to execute, for example, eat()
#     def wantsToEat(self,
#                    philosopher: int,
#                    pickLeftFork: 'Callable[[], None]',
#                    pickRightFork: 'Callable[[], None]',
#                    eat: 'Callable[[], None]',
#                    putLeftFork: 'Callable[[], None]',
#                    putRightFork: 'Callable[[], None]') -> None:
#         # Take the right fork, then left fork
#         self.forks[philosopher].acquire()
#         self.forks[(philosopher + 1) % 5].acquire()
 
#         # Eat!
#         pickRightFork()
#         pickLeftFork()
#         eat()
#         putRightFork()
#         putLeftFork()
 
#         # Release right fork, then left fork
#         self.forks[philosopher].release()
#         self.forks[(philosopher + 1) % 5].release()
# from collections import Counter
list1 = [0, 1, 2, 3, 4, 5, 0] # answer
# col = Counter(list1)
col = list1.count(0)
print(col)
# list2 = [1, 2, 4, 3, 5, 1]

# result =  all(elem in list2  for elem in list1)
# if result:
#     print("Yes, list1 contains all elements in list2")    
# else :
#     print("No, list1 does not contains all elements in list2")