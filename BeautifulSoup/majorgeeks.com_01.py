# https://www.majorgeeks.com
# https://www.majorgeeks.com/files/page/2.html # more pages

from bs4 import BeautifulSoup 
import html
import re
import requests
import os

os.system('cls' if os.name=='nt' else 'clear')

url = "https://www.majorgeeks.com"
htmlfile = 'majorgeeks.com.html'


def get_page(choice):

	if choice.lower() == "local":
		# Local
		with open(htmlfile, 'r', errors='ignore') as f:
		   data = f.read();
		   f.close


	elif choice.lower() == "net":
		# Internet:
		data = str(requests.get(url).content)
		
	else:
	
		print("Nothing To Do!")
		input()
		exit(1)
		
	return data
		


### START HERE

# Choose between "Local" OR "Net"

data = get_page("local")



# Add unique part of favourite app name here to be warned of updates
watch_words = ["notepad++", "miranda", "sysgauge", "chromium"] 
watching = []

software = []

# Get only the divs we need
# earlier divs are adverts.

data = re.search("<!-- Template: files_day_rss_header -->.*", \
				data, re.DOTALL).group(0)   


# Parse HTML Code
soup = BeautifulSoup(data, 'html.parser')


# Multiple classes of div:
divs = soup.find_all('div', class_=['geekytitle', 'geekyinsidecontent'])


for div in divs: #[:2]

	description =""

	# For geekytitle:
	if "geekytitle" in str(div):
		title = div.get_text().strip()

	# For geekyinsidecontent:
	# Want main text but not text in added links:
	if "geekyinsidecontent" in str(div):
		description = re.search(">(.*?)<", str(div), re.DOTALL).group(1).strip()
	
	
	if description and title:
		software.append([title, description])
		
		for word in watch_words:
		
			if word.lower() in title.lower():
		
				watching.append([title, description])


# OUTPUT:

# Latest Date:
lastupdate = soup.find('div', class_='geekydate').get_text().strip()
dash = "-"

print(f"\nLast Updated: {lastupdate} \
\nTotal Files:  {int(len(divs) / 2)} \
\n{dash * 31}\n")


# Main List:

# Print only each page to console.
# Remove outer range loop for all.

count = 0

for x in range(0, len(software), 20):

	for each in software[x:x+20]: # Remove [] for All.
		
		count+=1
		
		print(f"{count}: {each[0]}:\n\n{each[1]}\n=================")
		
	print(f"\n\nShowing: {x} to {count} of {len(software)}\n"
			+ "Next Page: Press Enter.")
			
	input()



#Watched
print("\n\n* Watched Software: *\n-----------------------")	
for each in watching:

	print(f"{each[0]}:\n\n{each[1]}\n=================")
	
	
	
input()