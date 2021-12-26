from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
search = driver.find_element_by_name("q")
search.send_keys("teste")
search.send_keys(Keys.RETURN)
time.sleep(2)

results = driver.find_element_by_id("rso")
results.find_elements_by_class_name("LC20lb MBeuO DKV0Md")
print(results.text)
time.sleep(5)

driver.quit()