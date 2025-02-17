# Python 3
# delete_duplicate_files.py

import os 
import hashlib 
import glob


#files = glob.glob("*.*")

# , reverse=True, key=str.casefold
# Alphabetically Reversed files - In case you want to 
# delete the longer filename first.

files = sorted(glob.glob("*.*"), reverse=True, key=str.casefold)

unique_files = dict()

counter = 0


print(f"Processing {len(files)} files\n\n")



for file in files: 

	
	Hash_file = hashlib.md5(open( 
		file,'rb').read()).hexdigest() 
		

	if Hash_file not in unique_files: 

		unique_files[Hash_file] = file
		
	else: 
		os.remove(file) 
		
		counter += 1
		
		print(f"Del: {file}")
		



print(f"\n\nDeleted {counter} files\n\n")
	

input()	