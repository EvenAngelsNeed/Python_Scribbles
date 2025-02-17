# Python 3+

import subprocess
import time


command = r'notepad'


print("\nClose Running Program to get Return Code.")

# subprocess.run is blocking.
output = subprocess.run(command, shell=True)


print(f"Return Code: {output.returncode}\n")
		

# ------------------------------

print("\nAnother Example Using Poll:\nTesting If App Still Running.\n")	

# subprocess.Popen is non blocking.
output = subprocess.Popen(command)

while output.poll() is None:
	
    print('Still Active')
    
    time.sleep(2)


if output.poll() > 0:

	print(f"Error with command:\n{command}\n")
	
else:

	print('\nClosed. Exited with returncode %d' \
				% output.returncode) 
				
				# Or use output.poll() - Gives returncode as well.

input()


    

