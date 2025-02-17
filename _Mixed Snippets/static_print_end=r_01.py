import time
import os

os.system("cls")

print("\n\n")


def countdown(time_sec):

    while time_sec:
    
        mins, secs = divmod(time_sec, 60)
        
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        
        print("\t" + timeformat, end='\r')
        
        time.sleep(1)
        
        time_sec -= 1

    print("     ", end='\r')


countdown(5)

# -------------------------


time.sleep(3)


print("\tHello", end='\r')

time.sleep(3)

print("\tWorld", end='\r')

# -------------------------


time.sleep(3)	

words = [
"\tYou give but little",
"\twhen you give of your possessions.",

"\tIt is when you give of yourself",
"\tthat you truly give."
] # Khalil Gibran.


clear = "\t" + " " * len(max(words, key = len))

for word in words:

	print(word, end='\r')

	time.sleep(4)

	print(clear, end='\r')






input("\nEnter To Exit...")