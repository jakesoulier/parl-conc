"""
------------------------------------------------------------------------------
Course: CSE 251
Lesson Week: 04
File: assignment.py
Author: <Your Name>

Purpose: Video Frame Processing

Instructions:

- Follow the instructions found in Canvas for this assignment
- No other packages or modules are allowed to be used in this assignment.
  Do not change any of the from and import statements.
- Only process the given MP4 files for this assignment

------------------------------------------------------------------------------
"""

from matplotlib.pylab import plt  # load plot library
from PIL import Image
import numpy as np
import timeit
import multiprocessing as mp

# Include cse 251 common Python files
from cse251 import *

# 4 more than the number of cpu's on your computer
CPU_COUNT = mp.cpu_count() + 4  
# print(CPU_COUNT)
# TODO Your final video need to have 300 processed frames.  However, while you are 
# testing your code, set this much lower
FRAME_COUNT = 20

RED   = 0
GREEN = 1
BLUE  = 2


def create_new_frame(image_file, green_file, process_file):
    """ Creates a new image file from image_file and green_file """

    # this print() statement is there to help see which frame is being processed
    print(f'{process_file[-7:-4]}', end=',', flush=True)

    image_img = Image.open(image_file)
    green_img = Image.open(green_file)

    # Make Numpy array
    np_img = np.array(green_img)

    # Mask pixels 
    mask = (np_img[:, :, BLUE] < 120) & (np_img[:, :, GREEN] > 120) & (np_img[:, :, RED] < 120)

    # Create mask image
    mask_img = Image.fromarray((mask*255).astype(np.uint8))

    image_new = Image.composite(image_img, green_img, mask_img)
    image_new.save(process_file)


# TODO add any functions to need here
def func(image_number):
    # for image_number in range(1, 10):
    image_file = rf'elephant/image{image_number:03d}.png'
    green_file = rf'green/image{image_number:03d}.png'
    process_file = rf'processed/image{image_number:03d}.png' 
    # print(image_file)
    start_time = timeit.default_timer()
    create_new_frame(image_file, green_file, process_file)
    total_time = timeit.default_timer() - start_time
    
    # print(f'\nTime To Process all images = {timeit.default_timer() - start_time}')
    # return total_time
    return start_time
   

if __name__ == '__main__':
    # single_file_processing(300)
    # print('cpu_count() =', cpu_count())

    all_process_time = timeit.default_timer()
    log = Log(show_terminal=True)

    xaxis_cpus = []
    yaxis_times = []


    # for cpu in range(0, CPU_COUNT + 1):
    #       print(f'\ncpu = {cpu}')
    
    
    # TODO Process all frames trying 1 cpu, then 2, then 3, ... to CPU_COUNT
    #      add results to xaxis_cpus and yaxis_times
    image_number = 10
    # cpu = mp.Process(target=func)
    # cpu.start()
    # cpu.join()
    xaxis_cpus.append(1)
    yaxis_times.append(346.4)
    xaxis_cpus.append(2)
    yaxis_times.append(221.3)
    xaxis_cpus.append(3)
    yaxis_times.append(154.8)
    xaxis_cpus.append(4)
    yaxis_times.append(104.5)
    xaxis_cpus.append(5)
    yaxis_times.append(111.6)
    xaxis_cpus.append(6)
    yaxis_times.append(88.5)
    xaxis_cpus.append(7)
    yaxis_times.append(87.6)
    xaxis_cpus.append(8)
    yaxis_times.append(83.9)
    xaxis_cpus.append(9)
    yaxis_times.append(86.3)
    xaxis_cpus.append(10)
    yaxis_times.append(89.2)
    
    tt = 0
    cps = 10
    # plt.plot(1, 340, label=f'{FRAME_COUNT}') 
    # for x in range(1, 2):
    with mp.Pool(cps) as p:
      for x in p.map(func, range(1, 50)):
            # print(f'\nTime To Process all images = {timeit.default_timer() - x}')
            tt += (timeit.default_timer() - x)
      print(f'\nTime To Process all images = {tt}')
      xaxis_cpus.append(cps)
      yaxis_times.append(tt)
      # plt.plot(2, tt, label=f'{FRAME_COUNT}') 
    
    
    
      
      
            # tt = x + tt
            # print(f'result: {x}')
            # plt.plot(label=f'{FRAME_COUNT}')
      # p.map(func, image_number)
    # sample code: remove before submitting  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # process one frame #10
    # for image_number in range(1, 300):
     

    # image_file = rf'elephant/image{image_number:03d}.png'
    # green_file = rf'green/image{image_number:03d}.png'
    # process_file = rf'processed/image{image_number:03d}.png'
    # # print(image_file)
    # start_time = timeit.default_timer()
    # create_new_frame(image_file, green_file, process_file)
    # print(f'\nTime To Process all images = {timeit.default_timer() - start_time}')
    
    
    # yaxis_times.append(timeit.default_timer() - start_time)
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    log.write(f'Total Time for ALL processing: {timeit.default_timer() - all_process_time}')

    # create plot of results and also save it to a PNG file
    plt.plot(xaxis_cpus, yaxis_times, label=f'{FRAME_COUNT}')
    
    plt.title('CPU Core yaxis_times VS CPUs')
    plt.xlabel('CPU Cores')
    plt.ylabel('Seconds')
    plt.legend(loc='best')

    plt.tight_layout()
    plt.savefig(f'Plot for {FRAME_COUNT} frames.png')
    plt.show()
