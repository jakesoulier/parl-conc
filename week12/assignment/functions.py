"""
Course: CSE 251, week 12
File: common.py
Author: <your name>

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

<Add your comments here>


Describe how to speed up part 2

<Add your comments here>


10% Bonus to speed up part 3

<Add your comments here>

"""
from common import *

# -----------------------------------------------------------------------------
def depth_fs_pedigree(family_id, tree):
    # add person to tree
    print(f'fam id: {family_id}')
    person_t = Request_thread(f'{TOP_API_URL}/person/{family_id}')
    person_t.start()
    person_t.join()
    if("id" not in person_t.response):
        return
    person = Person(person_t.response)
    if(not tree.does_person_exist(person)):
        tree.add_person(person)

    # add family to tree, need to join here to get the response
    family_t = Request_thread(f'{TOP_API_URL}/family/{family_id}')
    family_t.start()
    family_t.join()
    if("id" not in family_t.response):
        return
    family = Family(family_id, family_t.response)
    print(family.children)
    # if(not tree.does_family_exist(family)):
    #     tree.add_family(family)
    for kid in family.children:
        print(kid)
        # depth_fs_pedigree(kid, tree)
        # pass

# -----------------------------------------------------------------------------
def breadth_fs_pedigree(start_id, tree):
    # TODO - implement breadth first retrieval

    print('WARNING: BFS function not written')

    pass


# -----------------------------------------------------------------------------
def breadth_fs_pedigree_limit5(start_id, tree):
    # TODO - implement breadth first retrieval
    #      - Limit number of concurrent connections to the FS server to 5

    print('WARNING: BFS (Limit of 5 threads) function not written')

    pass
