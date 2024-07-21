# python 3.7+
# basic-get-webpage-01.py

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Using webdriver_manager to avoid complaint about no firefox version.

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.google.com')

	#
	# Do your work on the page here.
	#

input() # Press enter. # Just here to hold browser open for moment.

driver.quit()