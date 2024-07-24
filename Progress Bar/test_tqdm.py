# python3
# test_tqdm.py

import time
import tqdm


print('\nBasic Usage:\n')

# Basic Usage:
a=0

for i in tqdm.tqdm(range(10)):
    
    # Do some processing here:
    a += 1
    
    time.sleep(0.1)
    
print("done!\n")
print(a)

print('\nUsing descriptions:\n')

# Descriptions:
for i in tqdm.tqdm(range(10), desc="Description Here"):
    
	# Do some processing here:
    time.sleep(0.1)

print("done!\n\n")

print('\nUsing nested loops:\n')

# Nested Loops:
for outer in tqdm.tqdm([10, 20, 30, 40], desc="Outer Loop"):

	# Do some processing here:
	    
    for inner in tqdm.tqdm(range(outer), desc="Inner Loop", position=1, leave=False):

		# Do some processing here:    
        time.sleep(0.1)

print("done!\n\n")

print('\nSet description in loop:\n')

# Set description in loop:
import glob # New import just for this section.

patern = ".\*.*" # Change folder\*.* to whatever.
files = tqdm.tqdm(glob.glob(patern))


for file in files:
    files.set_description(file)
    
    # Do some processing here:    
    time.sleep(0.5)


print("done!\n\n")

print('\nPrint using: tqdm.tqdm.write("string"):\n')

# Keep tqdm from showing a new bar if wanting to print().
# Use tqdm.tqdm.write("string") instead of print().

for i in tqdm.tqdm(range(10)):
    
	tqdm.tqdm.write("Task: " + str(i)) # Only strings
	
    # Do some processing here:
	time.sleep(0.1)

    
print("done!\n\n")

print("\nAs above but using inbuilt 'trange' instead of 'range':\n")

# Using trange instead of range

from tqdm import trange # New import just for this section.

for i in trange(10):

	tqdm.tqdm.write("Task: " + str(i))

	# Do some processing here:	
	time.sleep(0.1)  
	
    
print("done!\n\n")


input()