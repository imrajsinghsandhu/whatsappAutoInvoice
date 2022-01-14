from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/Users/Imraj/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')

# Register the driver
chrome_browser = webdriver.Chrome(executable_path='/Users/Imraj/Desktop/Drivers/chromedriver', options=options)
chrome_browser.get('https://www.google.com')

def second_product():

    def helper():
        try:
            client_name = WebDriverWait(chrome_browser, 2).until(EC.presence_of_element_located((By.XPATH, '//div[@data-hook="shipping-customer-name"]')))
            return client_name.text
        except:
            return ''
    return helper()

print(second_product())