import selenium
from selenium import webdriver
from selenium.webdriver import ChromeOptions
hub = 'http://selenium-hub:4444'
webA = 'http://webA:3000'
driver = webdriver.Remote(command_executor=hub, options=ChromeOptions())
driver.set_page_load_timeout(5)
input("Press Enter to continue...")
driver.get(webA)
print(driver.current_url)
driver.quit()