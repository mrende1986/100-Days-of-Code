from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/mattrende/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=104116056&keywords=python%20developer&location=Carlsbad%2C%20California%2C%20United%20States")

time.sleep(3)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(3)
username = driver.find_element_by_name("session_key")
username.send_keys("mrende@gmail.com")
password = driver.find_element_by_name("session_password")
password.send_keys("493Yates")
password.send_keys(Keys.ENTER)

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

# time.sleep(2)
# next_button = driver.find_element_by_css_selector(".display-flex button")
# next_button.click()

# time.sleep(2)
# review_button = driver.find_element_by_id("ember442")
# review_button.click()

time.sleep(2)
follow_company = driver.find_element_by_id("follow-company-checkbox")
follow_company.click()

time.sleep(2)
submit = driver.find_element_by_id("ember456")
submit.click()