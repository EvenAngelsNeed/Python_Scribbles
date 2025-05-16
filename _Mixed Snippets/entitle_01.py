# -*- coding: utf-8 -*-
# python3

# Make Title case whilst preserving upper case as in OK EU GB

import re

def entitle(data):

	data = " ".join([c.title() if c.islower() else c for c in data.split()])

	return data


print("\nOriginal:  ", "every thiNg is OK.\n")

print("Title Case:", entitle("every thing is OK."))



input("\n\nEnter to Exit")
