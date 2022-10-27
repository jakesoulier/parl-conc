"""
Course: CSE 251
Lesson Week: 07
File: assignment.py
Author: <Your name here>
Purpose: Processing Plant
Instructions:
- Implement the classes to allow gifts to be created.
"""

import random
import multiprocessing as mp
import os.path
import time
import datetime

# Include cse 251 common Python files - Don't change
from cse251 import *

CONTROL_FILENAME = 'settings.txt'
BOXES_FILENAME   = 'boxes.txt'

# Settings consts
MARBLE_COUNT = 'marble-count'
CREATOR_DELAY = 'creator-delay'
BAG_COUNT = 'bag-count'
BAGGER_DELAY = 'bagger-delay'
ASSEMBLER_DELAY = 'assembler-delay'
WRAPPER_DELAY = 'wrapper-delay'

# No Global variables

class Bag():
    """ bag of marbles - Don't change """

    def __init__(self):
        self.items = []

    def add(self, marble):
        self.items.append(marble)

    def get_size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Gift():
    """ Gift of a large marble and a bag of marbles - Don't change """

    def __init__(self, large_marble, marbles):
        self.large_marble = large_marble
        self.marbles = marbles

    def __str__(self):
        marbles = str(self.marbles)
        marbles = marbles.replace("'", "")
        return f'Large marble: {self.large_marble}, marbles: {marbles[1:-1]}'


class Marble_Creator(mp.Process):
    """ This class "creates" marbles and sends them to the bagger """

    colors = ('Gold', 'Orange Peel', 'Purple Plum', 'Blue', 'Neon Silver', 
        'Tuscan Brown', 'La Salle Green', 'Spanish Orange', 'Pale Goldenrod', 'Orange Soda', 
        'Maximum Purple', 'Neon Pink', 'Light Orchid', 'Russian Violet', 'Sheen Green', 
        'Isabelline', 'Ruby', 'Emerald', 'Middle Red Purple', 'Royal Orange', 'Big Dip O’ruby', 
        'Dark Fuchsia', 'Slate Blue', 'Neon Dark Green', 'Sage', 'Pale Taupe', 'Silver Pink', 
        'Stop Red', 'Eerie Black', 'Indigo', 'Ivory', 'Granny Smith Apple', 
        'Maximum Blue', 'Pale Cerulean', 'Vegas Gold', 'Mulberry', 'Mango Tango', 
        'Fiery Rose', 'Mode Beige', 'Platinum', 'Lilac Luster', 'Duke Blue', 'Candy Pink', 
        'Maximum Violet', 'Spanish Carmine', 'Antique Brass', 'Pale Plum', 'Dark Moss Green', 
        'Mint Cream', 'Shandy', 'Cotton Candy', 'Beaver', 'Rose Quartz', 'Purple', 
        'Almond', 'Zomp', 'Middle Green Yellow', 'Auburn', 'Chinese Red', 'Cobalt Blue', 
        'Lumber', 'Honeydew', 'Icterine', 'Golden Yellow', 'Silver Chalice', 'Lavender Blue', 
        'Outrageous Orange', 'Spanish Pink', 'Liver Chestnut', 'Mimi Pink', 'Royal Red', 'Arylide Yellow', 
        'Rose Dust', 'Terra Cotta', 'Lemon Lime', 'Bistre Brown', 'Venetian Red', 'Brink Pink', 
        'Russian Green', 'Blue Bell', 'Green', 'Black Coral', 'Thulian Pink', 
        'Safety Yellow', 'White Smoke', 'Pastel Gray', 'Orange Soda', 'Lavender Purple',
        'Brown', 'Gold', 'Blue-Green', 'Antique Bronze', 'Mint Green', 'Royal Blue', 
        'Light Orange', 'Pastel Blue', 'Middle Green')

    def __init__(self, conn, marble_count):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        # self.marble = marble
        # self.colors = colors
        self.conn = conn
        self.marble_count = marble_count

    def run(self):
        '''
        for each marble:
            send the marble (one at a time) to the bagger
              - A marble is a random name from the colors list above
            sleep the required amount
        Let the bagger know there are no more marbles
        '''
        for x in range(self.marble_count):
            marble = random.choice(self.colors)
            self.conn.send(marble)
            
        self.conn.send('DONE')
        
        


class Bagger(mp.Process):
    """ Receives marbles from the marble creator, then there are enough
        marbles, the bag of marbles are sent to the assembler """
    def __init__(self, connMarble, connAssem, marble_count, bag_count):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.marbles = {}
        self.connMarble = connMarble
        self.connAssem = connAssem
        self.marble_count = marble_count
        self.bag_count = bag_count

    def run(self):
        '''
        while there are marbles to process
            collect enough marbles for a bag
            send the bag to the assembler
            sleep the required amount
        tell the assembler that there are no more bags
        '''
        # while 'DONE' not in self.marbles:
        for x in range(7):
            # self.marbles.append(self.connMarble.recv())
            # self.marbles['marbles'] = self.connMarble.recv()
            if 'marbles' not in self.marbles:
                self.marbles['marbles'] = []
                self.marbles['marbles'].append(self.connMarble.recv())
            else:
                self.marbles['marbles'].append(self.connMarble.recv())
            # thisdict.update({"color": "red"})
            # print(f'marbles in dict: {self.marbles}')
            if len(self.marbles['marbles']) == self.bag_count:
                # print(self.marbles)
                self.connAssem.send(self.marbles)
        # self.connAssem.send('DONE')
        


class Assembler(mp.Process):
    """ Take the set of marbles and create a gift from them.
        Sends the completed gift to the wrapper """
    marble_names = ('Lucky', 'Spinner', 'Sure Shot', 'The Boss', 'Winner', '5-Star', 'Hercules', 'Apollo', 'Zeus')

    def __init__(self, connBag, connWrap):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.connBag = connBag
        self.connWrap = connWrap
        # self.gift = {}

    def run(self):
        '''
        while there are bags to process
            create a gift with a large marble (random from the name list) and the bag of marbles
            send the gift to the wrapper
            sleep the required amount
        tell the wrapper that there are no more gifts
        '''
        # while 'DONE' not in self.gift:
        name = random.choice(self.marble_names)
        gift = self.connBag.recv()
        gift['large'] = name
        self.connWrap.send(gift)
        # print(f'gift: {gift}')
        # self.gift = self.connBag.recv()
        # self.gift.append(name)
        # self.connWrap.send(self.gift)
        # self.gift.append(self.connBag.recv())
        
        # print(f'Assembler gift: {self.gift}')
        # name.append(self.connBag.recv())
        # print(f'Assembler recieve: {self.connBag.recv()}')
            # self.gift.append(self.connBag.recv())
        # print(self.gift)


class Wrapper(mp.Process):
    """ Takes created gifts and wraps them by placing them in the boxes file """
    def __init__(self, connBag):
        mp.Process.__init__(self)
        # TODO Add any arguments and variables here
        self.connBag = connBag
        self.filename = 'boxes.txt'

    def run(self):
        '''
        open file for writing
        while there are gifts to process
            save gift to the file with the current time
            sleep the required amount
        '''
        inputted = self.connBag.recv()
        print(f'wrap recieved: {inputted}')
        # inputted = " ".join(inputted)
        
        marbles = ", ".join(inputted['marbles'])
        # print(f'time: {datetime.now().time()}')
        with open('boxes.txt', 'w') as f:
            f.write("Created - " + str(datetime.now().time()) + ": Large marble: " + inputted['large'] + ', marbles: ' + marbles)
        
        


def display_final_boxes(filename, log):
    """ Display the final boxes file to the log file -  Don't change """
    if os.path.exists(filename):
        log.write(f'Contents of {filename}')
        with open(filename) as boxes_file:
            for line in boxes_file:
                log.write(line.strip())
    else:
        log.write_error(f'The file {filename} doesn\'t exist.  No boxes were created.')



def main():
    """ Main function """

    log = Log(show_terminal=True)

    log.start_timer()

    # Load settings file
    settings = load_json_file(CONTROL_FILENAME)
    if settings == {}:
        log.write_error(f'Problem reading in settings file: {CONTROL_FILENAME}')
        return

    log.write(f'Marble count                = {settings[MARBLE_COUNT]}')
    log.write(f'settings["creator-delay"]   = {settings[CREATOR_DELAY]}')
    log.write(f'settings["bag-count"]       = {settings[BAG_COUNT]}') 
    log.write(f'settings["bagger-delay"]    = {settings[BAGGER_DELAY]}')
    log.write(f'settings["assembler-delay"] = {settings[ASSEMBLER_DELAY]}')
    log.write(f'settings["wrapper-delay"]   = {settings[WRAPPER_DELAY]}')

    # TODO: create Pipes between creator -> bagger -> assembler -> wrapper
    creat2bag, bag2create = mp.Pipe()
    bag2assem, assem2bag = mp.Pipe()
    assem2wrap, wrap2assem = mp.Pipe()
    # TODO create variable to be used to count the number of gifts
    gift_count = 0
    # delete final boxes file
    if os.path.exists(BOXES_FILENAME):
        os.remove(BOXES_FILENAME)

    log.write('Create the processes')
    MARBLE_COUNT_EX = 10
    # TODO Create the processes (ie., classes above)
    marble = Marble_Creator(creat2bag, MARBLE_COUNT_EX)
    bagger = Bagger(bag2create, bag2assem, MARBLE_COUNT_EX, settings[BAG_COUNT])
    assembler = Assembler(assem2bag, assem2wrap)
    wrapper = Wrapper(wrap2assem,)
    # marble = mp.Process(target=Marble_Creator, args=(creator,))
    # bagger_creat = mp.Process(target=Bagger, args=(bagger,))
    log.write('Starting the processes')
    # TODO add code here
    marble.start()
    bagger.start()
    assembler.start()
    wrapper.start()
    log.write('Waiting for processes to finish')
    # TODO add code here
    marble.join()
    bagger.join()
    assembler.join()
    wrapper.join()
    # display_final_boxes(BOXES_FILENAME, log)

    # TODO Log the number of gifts created.



if __name__ == '__main__':
    main()

