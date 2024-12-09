# https://www.snapfiles.com/new/list-freeware-whatsnew.html
# https://www.snapfiles.com/new/list-freeware-whatsnew2.html # in case need to get more pages

from bs4 import BeautifulSoup 
import html
import re
import os
import requests

os.system('cls' if os.name=='nt' else 'clear')

data = requests.get('https://www.snapfiles.com/new/list-freeware-whatsnew.html').content

#htmlfile = 'snapfiles_01.html'

#with open(htmlfile, 'r', errors='ignore') as f:
#   data = f.read();
#   f.close


# add unique part of favourite app name here to be warned of updates
watch_words = ["notepad++", "miranda", "sysgauge"] 


# Parse HTML Code
soup = BeautifulSoup(data, 'html.parser')

table = soup.find("table")

updated =  soup.find_all(class_="wn-daterow")
appicon = soup.find_all(class_="appicon")
introtext = soup.find_all(class_="introtext")
appversion = soup.find_all(class_="mp-appversion")
detailview = soup.find_all(class_="featuredetailview")

print("\nSnapFiles:\n\nTotal Apps =", len(appicon))

print(f"\nLatest Updates For: {updated[-1].text} - {updated[0].text}")

print("\n=====================")



watching = []

for idx in range(0, len(appicon)):

	img = appicon[idx].find('img', alt=True)
	print(f"App {idx+1}:\t", img['alt'])
	
	
	for word in watch_words:
		if word.lower() in img['alt'].lower():
		
			watching.append([idx+1, img['alt'], appversion[idx].text])

	
	
	print("About:\t", introtext[idx].text.replace("  ", "").strip().title().split("\n")[-1])
	
	print("Ver:\t", appversion[idx].text)
	
	detail = detailview[idx].text.replace("\t", "").replace("\n\n", "")
	
	detail = re.search("O/s:(.*?)File Size:(.*?)Price:(.*?)Pop", detail, re.DOTALL)	


	print("\nInfo:", end='')
	
	print("\t", detail.group(1))
	print("\t", detail.group(2).strip())
	print("\t", detail.group(3))

		
	print("=====================")
	


if watching and watch_words:
	print("\n\n********************************")
	print("* Alert: Apps You're Watching: *")	
	print("********************************\n")
	for each in watching:
		print("*", str(each).strip("[]"))
		



print("\n\n=====================\n\n")

input()
