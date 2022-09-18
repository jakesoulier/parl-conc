![](../../site/banner.png)

# 01 Prove: Creating Threads 

# Overview

Your first assignment is to create a program that will compute the sum of numbers from 1 to a given number. Your program will need to perform this function in two ways. First, it should sum the numbers using a class that extends the Thread class. Second, it should sum the numbers using the threading module and a global variable.

You will also be testing your program using a python Unit test. Testing your code is a very important skill to learn.

## Instructions

1. Read the `assignment01.py` and `assignment01-test.py` from the `week01/assignment` folder you cloned from Github. 
2. The python test file will test the following:
   A function that takes an integer number and a log object.
   Obtains the return values. The values will be the sum from using a class and sum from using a global (in that order).
   Ensure that the return values match the expected sums.
   You can run your code without having to execute the python unit test each time. Running it should test it using the number '10'.
3. You should print to a log the following:
   The number that you are summing up to: number={number} , where {number} is the passed in number
   In your class: Thread name, x={x-value}, sum={sum}  , where {x-value} is index of your loop, and {sum} is your summation variable
   In your threading function that is using a global: Thread name, x={x-value}, sum_global={sum_global}   , where {x-value} is index of your loop, and {sum_global} is your global summation variable
   A final statement showing the final sum of each.

   See example log below.
4. Submit both your code and your log file (no need to submit the unit test and please NO ZIP files).


## CSE 251 Logger

This assignment uses the Log class found in `cse251.py`. Refer to the [log class documentation](../overview/cse251_code.md). If you have properly installed the packages [CSE251 Installer](../overview/cse251_code.md), then the Log class can be resolved in your code.

The assignment program will creating the following logging information.  Here is an example of what your log file should look like.

```text
14:15:07| number=10
14:15:07| Thread-1, x=0, sum=0
14:15:07| Thread-1, x=1, sum=1
14:15:07| Thread-1, x=2, sum=3
14:15:07| Thread-1, x=3, sum=6
14:15:07| Thread-1, x=4, sum=10
14:15:07| Thread-1, x=5, sum=15
14:15:07| Thread-1, x=6, sum=21
14:15:07| Thread-1, x=7, sum=28
14:15:07| Thread-1, x=8, sum=36
14:15:07| Thread-1, x=9, sum=45
14:15:07| Thread-1, final sum using run=45
14:15:07| Thread-2 (sum_numbers), x=0, sum_global=0
14:15:07| Thread-2 (sum_numbers), x=1, sum_global=1
14:15:07| Thread-2 (sum_numbers), x=2, sum_global=3
14:15:07| Thread-2 (sum_numbers), x=3, sum_global=6
14:15:07| Thread-2 (sum_numbers), x=4, sum_global=10
14:15:07| Thread-2 (sum_numbers), x=5, sum_global=15
14:15:07| Thread-2 (sum_numbers), x=6, sum_global=21
14:15:07| Thread-2 (sum_numbers), x=7, sum_global=28
14:15:07| Thread-2 (sum_numbers), x=8, sum_global=36
14:15:07| Thread-2 (sum_numbers), x=9, sum_global=45
14:15:07| Thread-2 (sum_numbers), final sum using global=45
14:15:07| Return values from create_threads:
    actual_from_class=45, actual_from_thread_mod=45
14:15:07| number=13
14:15:07| Thread-3, x=0, sum=0
14:15:07| Thread-3, x=1, sum=1
14:15:07| Thread-3, x=2, sum=3
14:15:07| Thread-3, x=3, sum=6
14:15:07| Thread-3, x=4, sum=10
14:15:07| Thread-3, x=5, sum=15
14:15:07| Thread-3, x=6, sum=21
14:15:07| Thread-3, x=7, sum=28
14:15:07| Thread-3, x=8, sum=36
14:15:07| Thread-3, x=9, sum=45
14:15:07| Thread-3, x=10, sum=55
14:15:07| Thread-3, x=11, sum=66
14:15:07| Thread-3, x=12, sum=78
14:15:07| Thread-3, final sum using run=78
14:15:07| Thread-4 (sum_numbers), x=0, sum_global=0
14:15:07| Thread-4 (sum_numbers), x=1, sum_global=1
14:15:07| Thread-4 (sum_numbers), x=2, sum_global=3
14:15:07| Thread-4 (sum_numbers), x=3, sum_global=6
14:15:07| Thread-4 (sum_numbers), x=4, sum_global=10
14:15:07| Thread-4 (sum_numbers), x=5, sum_global=15
14:15:07| Thread-4 (sum_numbers), x=6, sum_global=21
14:15:07| Thread-4 (sum_numbers), x=7, sum_global=28
14:15:07| Thread-4 (sum_numbers), x=8, sum_global=36
14:15:07| Thread-4 (sum_numbers), x=9, sum_global=45
14:15:07| Thread-4 (sum_numbers), x=10, sum_global=55
14:15:07| Thread-4 (sum_numbers), x=11, sum_global=66
14:15:07| Thread-4 (sum_numbers), x=12, sum_global=78
14:15:07| Thread-4 (sum_numbers), final sum using global=78
14:15:07| Return values from create_threads:
    actual_from_class=78, actual_from_thread_mod=78
14:15:07| number=17
14:15:07| Thread-5, x=0, sum=0
14:15:07| Thread-5, x=1, sum=1
14:15:07| Thread-5, x=2, sum=3
14:15:07| Thread-5, x=3, sum=6
14:15:07| Thread-5, x=4, sum=10
14:15:07| Thread-5, x=5, sum=15
14:15:07| Thread-5, x=6, sum=21
14:15:07| Thread-5, x=7, sum=28
14:15:07| Thread-5, x=8, sum=36
14:15:07| Thread-5, x=9, sum=45
14:15:07| Thread-5, x=10, sum=55
14:15:07| Thread-5, x=11, sum=66
14:15:07| Thread-5, x=12, sum=78
14:15:07| Thread-5, x=13, sum=91
14:15:07| Thread-5, x=14, sum=105
14:15:07| Thread-5, x=15, sum=120
14:15:07| Thread-5, x=16, sum=136
14:15:07| Thread-5, final sum using run=136
14:15:07| Thread-6 (sum_numbers), x=0, sum_global=0
14:15:07| Thread-6 (sum_numbers), x=1, sum_global=1
14:15:07| Thread-6 (sum_numbers), x=2, sum_global=3
14:15:07| Thread-6 (sum_numbers), x=3, sum_global=6
14:15:07| Thread-6 (sum_numbers), x=4, sum_global=10
14:15:07| Thread-6 (sum_numbers), x=5, sum_global=15
14:15:07| Thread-6 (sum_numbers), x=6, sum_global=21
14:15:07| Thread-6 (sum_numbers), x=7, sum_global=28
14:15:07| Thread-6 (sum_numbers), x=8, sum_global=36
14:15:07| Thread-6 (sum_numbers), x=9, sum_global=45
14:15:07| Thread-6 (sum_numbers), x=10, sum_global=55
14:15:07| Thread-6 (sum_numbers), x=11, sum_global=66
14:15:07| Thread-6 (sum_numbers), x=12, sum_global=78
14:15:07| Thread-6 (sum_numbers), x=13, sum_global=91
14:15:07| Thread-6 (sum_numbers), x=14, sum_global=105
14:15:07| Thread-6 (sum_numbers), x=15, sum_global=120
14:15:07| Thread-6 (sum_numbers), x=16, sum_global=136
14:15:07| Thread-6 (sum_numbers), final sum using global=136
14:15:07| Return values from create_threads:
    actual_from_class=136, actual_from_thread_mod=136
```

## Rubric

Assignments are not accepted late. Instead, you should submit what you have completed by the due date for partial credit.

Assignments are individual and not team based.  Any assignments found to be  plagiarised will be graded according to the `ACADEMIC HONESTY` section in the syllabus. The Assignment will be graded in broad categories as outlined in the syllabus:

## Submission

When finished, upload your Python file to Canvas (please no ZIP files)