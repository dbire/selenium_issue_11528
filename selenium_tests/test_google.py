import selenium
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
hub = 'http://selenium-hub:4444'
webA = 'http://webA:3000'
driver = webdriver.Remote(command_executor=hub, options=ChromeOptions())
driver.get('http://www.google.com')
print(driver.current_url)
time.sleep(600)
driver.quit()