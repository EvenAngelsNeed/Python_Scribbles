# Tested On: py3.7 & Win7

# This should work if there is only one device attached.
# If more use:
# adb -s Android_Device_Name shell ls -l /sdcard/yourFolders/yourFilename.xyz

# File mod time has no seconds from ADB

import subprocess
import re
import os
import time


os.system('cls')


filename = "Database.kdbx"

local_path = "./" # or Blank = Script Folder # End with "/"
device_path = "/sdcard/Documents/_Data/" # End with "/"


device_get_datetime = f"adb shell ls -l {device_path}{filename}"

####### if file does not exist?

cmd_push = f"adb push {local_path}{filename} {device_path}"
cmd_pull = f"adb pull -a {device_path}{filename} {local_path}{filename}"

# -a = Preserve filedate # only preserves "Modified" not "Created"

regex = "(\d\d\d\d.\d\d.\d\d).*?(\d\d.\d\d)"


menu = \
"""
Menu:
------------------------------------------
* 1: Copy\Overwrite File on Mobile Device.

* 2: Copy\Overwrite File on This Computer.
------------------------------------------

Select 1 or 2 + Enter:

(Blank to Exit.)
"""



def connect(command):

	process = subprocess.Popen(command, stdout=subprocess.PIPE,stdin=subprocess.PIPE) #start adb and send commands

	adb_output = process.stdout.readlines() # Read adb_output from stdout

	# Pre processing list to remove byte state.
	adb_output = [item.decode("utf-8").strip('\r\n') for item in adb_output]

	return adb_output



def move_file():

	print()
	print(menu)

	direction = input(":>  ").lower()

	if direction == "1":

		# File Copied To Device

		adb_output = connect(cmd_push)

		print("\nOutput:\n")
		print(adb_output[0])

	elif direction == "2":

		# File Copied To Local

		adb_output = connect(cmd_pull)

		print("\nOutput:\n")
		print(adb_output[0])


	else:

		exit()


def do_adb():

	# File On Device:

	adb_output = connect(device_get_datetime)

	device_date_time = re.search(regex, adb_output[0]).group()


	# Local File:

	mtime = os.path.getmtime(local_path + filename)
	mtime = time.strptime(time.ctime(mtime))

	local_date_time = time.strftime("%Y-%m-%d %H:%M", mtime)



	print("\n\nFile: ",  filename)
	print()

	print("Last Modified:\n")

	print("Device: ", device_date_time)
	print("Local:  ", local_date_time)
	print('--------------------------\n')



	if device_date_time	== local_date_time:

		print("File Is Same Both Sides - Nothing To Do! (Y = Yes)\n")


		if input("Do you still want to copy the file? ").lower() == "y":

			move_file()

		else:

			exit()



	elif device_date_time	> local_date_time:

		print("File on Device is Newer\n\n" \
				"* Do You Want To Update The Local File?"	)

		move_file()



	else:

		print("File on Device is Older\n\n" \
				"* Do You Want To Update File On The Device?"	)

		move_file()










if __name__ == "__main__":
	do_adb()




print('\n\n---------------------')
input("Enter To Exit")