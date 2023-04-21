from selenium import webdriver

driver = webdriver.Chrome()
# to maximize the browser window
driver.maximize_window()
# get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
# to refresh the browser
driver.refresh()
# to close the browser
driver.close()
