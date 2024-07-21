#page-scrolling-keys-elements-01.py

from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

# Set up the Firefox WebDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Goto webpage with infinite scrolling
driver.get('https://reddit.com')
#driver.maximize_window()

# Function to scroll to bottom of page
def scroll_to_bottom():
    
    # Define number of times to scroll.
    # Here to avoid endless scrolling on some sites.
    # Remove the loop if needed.
    
    scroll_iterations = 4
    
    for _ in range(scroll_iterations):
    
        # Scroll down using the END key.
        ActionChains(driver).send_keys(Keys.END).perform()
        
        # Wait to allow content to load
        time.sleep(4)

# Call the function.
scroll_to_bottom()

input() # Press enter. Here just to hold browser open for moment.

# Close the browser window
driver.quit()

