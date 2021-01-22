from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
1. WebDriverWait is a class.
2. Explicit Wait -> we want to apply to a particular element
3. EC is a alias of expected conditions, to use all conditions if explicit wait
'''

driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.co.in/")
driver.find_element_by_class_name("uitk-faux-input").send_keys("Itarsi")
driver.find_element(By.XPATH, '//*[@id="location-field-destination-menu"]/div[2]/ul/li[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="wizard-hotel-pwa-v2-1"]/div[2]/div[2]/button').click()
driver.execute_script('window.scrollTo(0,300);')  # To scroll page 300 on Y axis
# Explicit Waits
wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable({By.ID, "popularFilter-1-OCEAN_VIEW"}))
element = wait.until(EC.presence_of_element_located((By.ID, 'popularFilter-1-OCEAN_VIEW')))





