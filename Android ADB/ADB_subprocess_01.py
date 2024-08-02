# Tested On: py3.7 & Win7

# Playing around with subprocess, ADB executable for Android
# and returning the output.

# Yet to add code to get devices should there 
# be more than one. But this should work if there 
# is only one device attached.

import subprocess
#import os

def connect(command):

	process = subprocess.Popen(command, stdout=subprocess.PIPE,stdin=subprocess.PIPE) #start adb and send commands

	lines = process.stdout.readlines() # Read lines from stdout
	
	# Pre processing list to remove byte state.
	
	lines = [item.decode("utf-8").strip('\r\n') for item in lines]
	
	return lines



def test():

	command = 'adb', 'shell', 'ls -f', 'sdcard' # []

	lines = connect(command)

	print()
	print(lines)
	print()

	# Sort output.

	lines.sort(key=str.lower) # Ascending avoiding casing issue.


	for line in lines:
		print(line)

	print('\n----------------\n')

	#---

	# Not using list for Popen command.

	command = 'adb shell ls -f sdcard/Music'

	lines = connect(command)

	lines.sort(key=str.lower) # Ascending avoiding casing issue.

	print()
	print(lines)
	print()

	for line in lines:
		print(line)
		
	print('\n----------------\n')

	#---

	# Not using list for Popen command.
	# Not using sort as it may mess up some outputs. As is:

	command = 'adb shell ls -lRas sdcard/music' # -Ras

	lines = connect(command)

	print()
	print(lines)
	print()

	for line in lines:
		print(line)
		
	print('\n----------------\n')

	input("Press Enter To Exit")
	exit()
	
	

if __name__ == "__main__":
	test()



# To-Do: Getting ready to make more functions.

adb = 'adb' # Path to r'c:\x\adb.exe' unless already in PATH.
shell = 'shell' # Obvious but maybe hard coded in some functions in future.
adb_cmd = 'ls -lRas' # Or whatever required.
source = 'sdcard/Music' # Or '' if not needed.
destination = r'c:\\temp' # Or '' if not needed.

command = [adb, shell, adb_cmd, source, destination]

# print()
# print(command)
# print()


def build_command():
	pass
	
def backup_user_apps():
	# And settings?
	pass


#input("Press Enter To Exit")