import platform
import os
import sys



print(platform.system())

print(os.name)

print(sys.platform)


# If needing more specific information:

#print(platform.version()) 
#print(platform.platform())





# Using platform:

if platform.system() == "Windows":

	# Windows code here:
	print("\nThis is a Windows System.")
	
	# win32_ver() only works on Windows
	# print(platform.win32_ver())


elif platform.system() == "Linux":

	# Linux code here:
	print("\nThis is a Linux System.")

	
elif platform.system() == "Darwin":

	# MacOS code here:
	print("\nThis is a MacOS System.")

	
else:
	print("\nUnknown System.")









# Outputs on different systems:


# macOS Sonoma 14.0
# ---------------------------------

#print(platform.system())
# Darwin

#print(os.name)
# posix

#print(sys.platform)
# darwin

#print(platform.release())
# 23.0.0

#print(platform.version())
# Darwin Kernel Version 23.0.0: Fri Sep 15 14:42:57 PDT 2023; root:xnu-10002.1.13~1/RELEASE_ARM64_T8112

#print(platform.platform())
# macOS-14.0-arm64-arm-64bit




# Windows 11:
# ---------------------------------

#print(platform.system())
# Windows

#print(os.name)
# nt

#print(sys.platform)
# win32

#print(platform.release())
# 10

#print(platform.version())
# 10.0.22621

#print(platform.platform())
# Windows-10-10.0.22621-SP0


#print(platform.win32_ver())
# ('10', '10.0.22621', 'SP0', 'Multiprocessor Free')

#print(platform.win32_is_iot())
# returns True for the IoT edition. Only in Python 3.8+



# Linux: Ubuntu 22:
# ---------------------------------

#print(platform.system())
# Linux

#print(os.name)
# posix

#print(sys.platform)
# linux

#print(platform.release())
# 5.15.0-86-generic

#print(platform.version())
# 96-Ubuntu SMP Wed Sep 20 08:23:49 UTC 2023

#print(platform.platform())
# Linux-5.15.0-86-generic-x86_64-with-glibc2.35






input()