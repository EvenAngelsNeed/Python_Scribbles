# python 3.7+
# basic-save-webpage-01.py

from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

import os
import codecs

# Using webdriver_manager to avoid complaint about no firefox version.

# Set geckodriver.exe.

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.implicitly_wait(0.5)
#driver.maximize_window()

# Launch URL.


driver.get('https://www.google.com')

# Obtain page source.
# We might need a function to scroll page to get all first.

html = driver.page_source


# File path to save page.

filepath = "page.html"

# Or use:
#filepath = os.path.join("C:\\temp","page.html")


# Open file in write mode with encoding.

with codecs.open(filepath, "w", "utf-8") as file:
	file.write(html)


#
# Do other work on the page in memory here.
#


input() # Press enter. # Just here to hold browser open for the moment.


#close browser.

driver.quit()




