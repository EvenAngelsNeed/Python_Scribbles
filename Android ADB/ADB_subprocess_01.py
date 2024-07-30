# Tested On: py3.7 & Win7

# Playing around with subprocess, ADB executable for Android
# and returning the output.

# Yet to add code to get devices should there 
# be more than one. But this should work if there 
# is only one device attached.

import subprocess
#import os


process = subprocess.Popen(['adb', 'shell', 'ls -f', 'sdcard'], stdout=subprocess.PIPE,stdin=
subprocess.PIPE) #start adb and send commands

lines=process.stdout.readlines() # Read lines from stdout

print()
print(lines)
print()

# Pre processing list to remove byte state then sort.

lines = [item.decode("utf-8").strip('\r\n') for item in lines]

lines.sort(key=str.lower) # Ascending avoiding casing issue.


for line in lines:
	print(line)

print()

#---

# Not using list for Popen command.

process = subprocess.Popen('adb shell ls -f sdcard/Music', stdout=subprocess.PIPE,stdin=
subprocess.PIPE) #start adb and send commands

lines=process.stdout.readlines() # Read lines from stdout

lines = [item.decode("utf-8").strip('\r\n') for item in lines]

lines.sort(key=str.lower) # Ascending avoiding casing issue.

print()
print(lines)
print()

for line in lines:
	print(line)
	
print()



input("Press Enter To Exit")


# To-Do: Getting ready to make a function.

adb = 'adb' # Path to c:\x\adb.exe unless already in Path
shell = 'shell' # Obvious but maybe hard coded in some functions in future.
adb_cmd = 'ls -f' # Or whatever required.
folder = 'sdcard/Music' # Or '' if needed.

command = [adb, shell, adb_cmd, folder]

def build_command():
	pass
	
