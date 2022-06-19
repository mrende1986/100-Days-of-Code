from selenium import webdriver
# from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/mattrende/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector('#articlecount a')
print(article_count.text)


driver.quit()