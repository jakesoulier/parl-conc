"""
Course: CSE 251, week 12
File: common.py
Author: Jake Soulier

Instructions:

Depth First Search
https://www.youtube.com/watch?v=9RHO6jU--GU

Breadth First Search
https://www.youtube.com/watch?v=86g8jAQug04


Requesting a family from the server:
family = Request_thread(f'{TOP_API_URL}/family/{id}')

Requesting an individual from the server:
person = Request_thread(f'{TOP_API_URL}/person/{id}')


You will lose 10% if you don't detail your part 1 
and part 2 code below

Describe how to speed up part 1

The main thing I did to speed up part 1 was using threads. The function would run
the needed tasks then call itself using recursion. To speed this up, I recalled the
function with a thread. I then did not start all the threads until later in the function.
I also used threads to get each person from the server. That way, I could
start each call and later join it so I had concurrency.


Describe how to speed up part 2

Part 2 was similar code. But, instead of using recursion, I just kept calling the function in 
a seperate loop and stopped the loop when both the wife and husband did not have any parents to
go to. It was speed up by still using threads to call the function everytime.


10% Bonus to speed up part 3

<Add your comments here>

"""
from common import *

# -----------------------------------------------------------------------------
def depth_fs_pedigree(family_id, tree):
    if family_id == None: # checks if family exists
        return
    # get family from server
    family_t = Request_thread(f'{TOP_API_URL}/family/{family_id}')
    family_t.start()
    family_t.join()
    family = Family(family_id, family_t.response)
    # add family to tree
    tree.add_family(family)
    # get husband from server
    husband_t = Request_thread(f'{TOP_API_URL}/person/{family.husband}')
    husband_t.start()
    # get wife from server
    wife_t = Request_thread(f'{TOP_API_URL}/person/{family.wife}')
    wife_t.start()
    # get kids from server
    kid_threads = []
    for kid in family.children:
        kid_t = Request_thread(f'{TOP_API_URL}/person/{kid}')
        kid_t.start()
        kid_threads.append(kid_t)
    # add husband to tree
    husband_t.join()
    response_hus = husband_t.response
    if(not tree.does_person_exist(response_hus['id'])):
        husband = Person(response_hus)
        tree.add_person(husband)
    # call function with parents id
    recurs_t = threading.Thread(target=depth_fs_pedigree, args=(husband.parents, tree))
    recurs_t.start()
    # add wife to tree
    wife_t.join()
    response_wif = wife_t.response
    if(not tree.does_person_exist(response_wif['id'])):
        wife = Person(response_wif)
        tree.add_person(wife)
    # call function with wife parents id
    recurs_t_w = threading.Thread(target=depth_fs_pedigree, args=(wife.parents, tree))
    recurs_t_w.start()
    # add kids to tree
    for t in kid_threads:
        t.join()
        response3 = t.response
        if(not tree.does_person_exist(response3['id'])):
            child = Person(response3)
            tree.add_person(child)

    recurs_t.join()
    recurs_t_w.join()
    
import queue
def createFamily(family_id, q, tree):
    if family_id == None: # checks if family exists
        return
    # get family from server
    family_t = Request_thread(f'{TOP_API_URL}/family/{family_id}')
    family_t.start()
    family_t.join()
    family = Family(family_id, family_t.response)
    # add family to tree
    tree.add_family(family)
    # get husband from server
    husband_t = Request_thread(f'{TOP_API_URL}/person/{family.husband}')
    husband_t.start()
    # get wife from server
    wife_t = Request_thread(f'{TOP_API_URL}/person/{family.wife}')
    wife_t.start()
    # get kids from server
    kid_threads = []
    for kid in family.children:
        kid_t = Request_thread(f'{TOP_API_URL}/person/{kid}')
        kid_t.start()
        kid_threads.append(kid_t)
    # add husband to tree
    husband_t.join()
    response_hus = husband_t.response
    if(not tree.does_person_exist(response_hus['id'])):
        husband = Person(response_hus)
        tree.add_person(husband)
    # checks if husband has parents
    if husband.parents != None:
        q.put(husband.parents) # add parents to queue

    # add wife to tree
    wife_t.join()
    response_wif = wife_t.response
    if(not tree.does_person_exist(response_wif['id'])):
        wife = Person(response_wif)
        tree.add_person(wife)
    # checks if wife has parents
    # checks if no more parents exist
    if wife.parents != None or (wife.parents == None and husband.parents == None):
        q.put(wife.parents) # adds wife parents to queue
    # add kids to tree
    for t in kid_threads:
        t.join()
        response3 = t.response
        if(not tree.does_person_exist(response3['id'])):
            child = Person(response3)
            tree.add_person(child)
    
# -----------------------------------------------------------------------------
def breadth_fs_pedigree(start_id, tree):
    # TODO - implement breadth first retrieval

    # starts queue
    q = queue.Queue()
    q.put(start_id)
    threads = []
    while True: # keeps looping until no more parents exist
        start_id = q.get()
        # stops loop
        if start_id == None:
            break
        # calls function
        t = threading.Thread(target=createFamily, args=(start_id, q, tree))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


# -----------------------------------------------------------------------------
def breadth_fs_pedigree_limit5(start_id, tree):
    # TODO - implement breadth first retrieval
    #      - Limit number of concurrent connections to the FS server to 5
    q = queue.Queue()
    q.put(start_id)
    threads = []
    lock = threading.Lock()
    while True: # keeps looping until no more parents exist
        start_id = q.get()
        # stops loop
        if start_id == None:
            break
        # calls function
        t = threading.Thread(target=createFamily, args=(start_id, q, tree))
        t.start()
        threads.append(t)
        if len(threads) == 5:
            lock.acquire()
            for x in range(5):
                t.join()
                threads.pop(0)
            # print(f'{threads}')
            lock.release()
    length = len(threads)
    # print(f'{length=}')
    for t in threads:
        t.join()
    

