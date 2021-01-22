import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
'''
1. At freshworks we r waiting for all footers links 
2. presence_of_all_elements_located -> 
3. Then get the message and click ok
4. alert_is_present() -> Checks and Switches to Alert also, returns reference of same alert
5. See JS_Alert_PopUp script, we used time.sleep there 
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
number_of_emps_element = driver.find_element(By.ID, 'Form_submitForm_NoOfEmployees')
select = Select(number_of_emps_element)
number_of_emps_list = select.options
print(number_of_emps_element.text)


