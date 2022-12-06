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
    if family_id == None:
        return
    family_t = Request_thread(f'{TOP_API_URL}/family/{family_id}')
    family_t.start()
    family_t.join()
    print(family_t.response)
    if("id" not in family_t.response):
        return
    person = Person(family_t.response)
    family = Family(family_id, person)
    tree.add_family(family)

    person_t = Request_thread(f'{TOP_API_URL}/person/{family.husband}')
    person_t.start()
    # person_t.join()
    person2_t = Request_thread(f'{TOP_API_URL}/person/{family.wife}')
    person2_t.start()

    kid_threads = []
    for kid in family.children:
        kid_t = Request_thread(f'{TOP_API_URL}/person/{kid}')
        kid_t.start()
        kid_threads.append(kid_t)

    person_t.join()
    response1 = person_t.response
    print(f'{response1=}')
    tree.add_person(response1)

    person2_t.join()
    response2 = person2_t.response
    print(f'{response2=}')
    tree.add_person(response2)

    for t in kid_threads:
        t.join()
        response3 = t.response
        if(not tree.does_person_exist(response3)):
            tree.add_person(response3)



    #MY ATTEMPT
    # if family_id == None:
    #     return
        
    # # count gen
    # gen = tree._count_generations(family_id)
    # # print(gen)
    # # print(f'fam_id! {family_id}')
    # # get person
    # person_t = Request_thread(f'{TOP_API_URL}/person/{family_id}')
    # person_t.start()
    # person_t.join()
    # if("id" not in person_t.response):
    #     return
    # person = Person(person_t.response)
    # # print(f'PERSON {person}')
    # # add person
    # if(not tree.does_person_exist(person)):
    #     # print(f'ADD {person.name}')
    #     tree.add_person(person)
    # # print(f'PERS - {person}')
    # # parent_t = Request_thread(f'{TOP_API_URL}/family/{person.parents}')
    # # parent_t.start()
    # # parent_t.join()
    # # if("id" not in parent_t.response):
    # #     return
    # # parent = Family(person.parents, parent_t.response)
    # # print(f'PARENT? {parent} for {person.name}')
    # # if(not tree.does_person_exist(parent)):
    # #     print(f'PARENT TO ADD? {parent.id}')
    # #     depth_fs_pedigree(parent, tree)


    # #add parents
    # # print(f'PERSON PARENT {person.parents}')
    # # if(person.parents != None):
    # #     depth_fs_pedigree(person.parents, tree)
    # # else:
    # #     print('no parent id')

    # # get parents
    # # parent_fam_t = Request_thread(f'{TOP_API_URL}/family/{person.parents}')
    # # parent_fam_t.start()
    # # parent_fam_t.join()
    # # if("id" not in parent_fam_t.response):
    # #     return
    # # parent_fam = Family(person.family, parent_fam_t.response)
    # # print(f'PARENT FAM: {parent_fam}')
    # # get family
    # family_t = Request_thread(f'{TOP_API_URL}/family/{person.family}')
    # family_t.start()
    # family_t.join()
    # if("id" not in family_t.response):
    #     return
    # family = Family(family_id, family_t.response)
    
    # # add wife
    # # print(f'WIFE COUNT- {family.wife}')
    # if(not tree.does_person_exist(family.wife)):
    #     depth_fs_pedigree(family.wife, tree)

    # # add husband parents
    

    # # add children
    # for child in family.children:
    #     if(not tree.does_person_exist(child)):
    #         depth_fs_pedigree(child, tree)

    # # add family
    # # print(f'FAMILIES {family}')
    # if(not tree.does_family_exist(family)):
    #     tree.add_family(family)

    #dads parents
    # print(f'PERSON: {person}')
    # print(f'PERSONPARENTS: {person.parents}')
    # depth_fs_pedigree(person.parents, tree)
    # parent_t = Request_thread(f'{TOP_API_URL}/person/{person.parents}')
    # parent_t.start()
    # parent_t.join()
    # if("id" not in parent_t.response):
    #     return
    # parent = Person(parent_t.response)
    # print(f'parent!: {parent}')
    
import queue
def createFamily(family_id, q, tree):
    pass 
    # copy dps code

# -----------------------------------------------------------------------------
def breadth_fs_pedigree(start_id, tree):
    # TODO - implement breadth first retrieval

    q = queue.Queue()
    q.put(start_id)
    threads = []
    while True:
        start_id = q.get()
        if start_id == None:
            break
        t = threading.Thread(target=createFamily, args=(start_id, q, tree))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


# -----------------------------------------------------------------------------
def breadth_fs_pedigree_limit5(start_id, tree):
    # TODO - implement breadth first retrieval
    #      - Limit number of concurrent connections to the FS server to 5
    pass
    

