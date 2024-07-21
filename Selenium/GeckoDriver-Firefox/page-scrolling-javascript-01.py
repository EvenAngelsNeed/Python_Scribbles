#page-scrolling-javascript-01.py

from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

import time


# Set up the firefox WebDriver
# Create webdriver instance
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


# Navigate to page

driver.get('https://www.reddit.com')


# Scroll down to the bottom of the page using javascript

last_height = driver.execute_script("return document.body.scrollHeight")

# Caution using this may cause endless scrolling on some deep dynamic web pages.

while True:

    # Scroll down to the bottom

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for page to load

    time.sleep(2)


    # Calculate new scroll height - compare with last scroll height

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:

        break

    last_height = new_height


# Close webdriver

driver.quit()

input()