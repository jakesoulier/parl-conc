from cmath import log
import pickle
import socket
import sys
import time
import unittest

from cse251 import Log

import assignment01 as tp

# Number:Expected Result
NUMBERS = {10: 45, 13: 78, 17: 136}


#########################
# DO NOT CHANGE THIS FILE
#########################

class TestFirstThreadProgram(unittest.TestCase):

    def test(self):
        results = []
        log = Log(show_terminal=True)

        for number, expected in NUMBERS.items():

            # call the code and get the results
            actual_from_class, actual_from_thread_mod = tp.create_threads(number, log)
            log.write(f'Return values from create_threads:\n\t{actual_from_class=}, {actual_from_thread_mod=}')
            
            try:
                # test that the results are integers
                self.assertTrue(isinstance(actual_from_class, int),
                                f"The return value ({actual_from_class}) should be an integer")
                self.assertTrue(isinstance(actual_from_thread_mod, int),
                                f"The return value ({actual_from_thread_mod}) should be an integer")
            except AssertionError as e:
                print(e)
                log.write_error("Test #1 failed, check console for reason")

            try:
                # test that the results are correct for both methods
                self.assertEqual(actual_from_class, expected,
                                 f"The sum from the class is incorrect (actual={actual_from_class}, expected={expected}): ")
                self.assertEqual(actual_from_thread_mod, expected,
                                 f"The sum from the class is incorrect (actual={actual_from_thread_mod}, expected={expected}): ")
            except AssertionError as e:
                print(e)
                log.write_error("Test #2 failed, check console for reason")
                
if __name__ == '__main__':
    unittest.main()
    # print(log)
