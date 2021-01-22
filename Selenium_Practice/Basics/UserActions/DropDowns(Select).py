from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")


def select_values(element, value):  # Function which accepts element, and the value of option which we want to select
    select1 = Select(element)
    time.sleep(5)
    select1.select_by_visible_text(value)


def select_from_dropdown(dropdown_options_list, value):
    print(len(dropdown_options_list))
    for e in dropdown_options_list:
        print(e.text)  # Prints text of all options of dropdown list
        if e == value:
            e.click()
            break


industry_element = driver.find_element(By.ID, "Form_submitForm_Industry")
select_values(industry_element, "Healthcare")  # Calling function
select = Select(industry_element)
industry_list = select.options
select_from_dropdown(industry_list, 'Automobile')
'''
It gives us all options in industry dropdown it is stored in a obj referred by industry_list
select.select_by_visible_text("Healthcare")  # Here Healthcare is a option in select dropdown
Select(driver.find_element(By.ID, "Form_submitForm_Industry")).select_by_visible_text("Healthcare") ---> Alternative
select.select_by_index(4) --> Will Select 4th value from dropdown
select.select_by_value("xyx") --> Will select by option which has value attribute as xyz
select.select_by_index(4)

------To Select Without using Select function-----------
driver.find_element(By.ID, "Form_submitForm_NoOfEmployees").click()
industry_list = driver.find_elements(By.XPATH, '//*[@id="Form_submitForm_NoOfEmployees"]/option')
for e in industry_list:
    #print(e.text)
    if e.text == '11 - 15':
        e.click()
        break
'''