# Python 3

import importlib.util
import os

os.system("cls")

print("Which Package Are You Looking For?\n")
package_name = input("Input ackage Name? ")

spec = importlib.util.find_spec(package_name)

print("\n\n")


if not spec:

	print("*", package_name + " is not installed.\n")
	
	
	out = input("Would you like to install: " + package_name \
					+ "\n\nUsing: pip install " \
					+ package_name + r" (y\n)").lower()
	
	
	command = f"pip install {package_name.lower()}"	
	
	
	if out == "y":
	
		result = os.system(command)
		
		print(result, out)
		
	else:
	
		print("\nNothing Installed.")
	

else:
	
	print("*", package_name + " is installed.\n")


	# Python < 3.8:
	#import pkg_resources

	#print("Version:", pkg_resources.get_distribution(package_name).version)


	# Python >= 3.8:
	from importlib.metadata import version

	print("Version:", version(package_name))


input()