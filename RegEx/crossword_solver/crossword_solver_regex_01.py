# python3
# Crossword Solver

# To do:
# Currently only British English - Other
# languages and spellings could be added.

# There are some issues in the wordlist being used.
# There might be missing or misspelt words.


import re

file = "wordlist01_uk.txt"

with open(file, 'r') as f:
	text = f.read()


def guess():
	print("\nInput a word to solve using full-stops\n"\
	      "(periods) for missing characters equal to the\n"\
	      "length of the word you are looking for:\n\n")

	word = input().lower()
	
	print("\nWord Length:", len(word), "\n")

	regex = f"^{word}$"

	found = re.findall(regex, text, flags=re.MULTILINE)


	for each in found: 
		
		print(each)

	x = input("\nTry again? - y/n:")

	if x in ['y','Y']:
		guess()


guess()

input("\nPress Enter To Exit:")