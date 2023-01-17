import selenium
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
hub = 'http://selenium-hub:4444'
driver = webdriver.Remote(command_executor=hub, options=ChromeOptions())
driver.get('http://www.google.com')
print(driver.current_url)
driver.quit()