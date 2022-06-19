from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/mattrende/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Matthew")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Rende")
email = driver.find_element_by_name("email")
email.send_keys("Matthew@gmail.com")

submit = driver.find_element_by_css_selector('form button')
submit.click()

# driver.quit()