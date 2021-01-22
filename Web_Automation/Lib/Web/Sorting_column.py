from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='G://Selenium//others//chromedriver_win32//chromedriver.exe')
driver.maximize_window()
driver.get('https://vantxqa.livmor.com/userLogin')
driver.implicitly_wait(10)
driver.find_element(By.ID, 'userId').send_keys('vantxqa.admin@livmor.com')
driver.find_element(By.ID, 'password').send_keys('Health@20')
driver.find_element(By.ID, 'btn_login').click()
time.sleep(2)

column_data_list = []
SORT_COLUMN_LOCATOR_COMMON = '//*[@id="PatientList"]/tbody/tr['
SORT_LAST_NAME_COLUMN = ']/td[1]/div'
SORT_FIRST_NAME_COLUMN = ']/td[2]/div'
SORT_CONTACT_COLUMN = ']/td[4]/div'
SORT_PATIENT_ID_COLUMN = ']/td[5]/div'
SORT_DEPARTMENT_COLUMN = ']/td[6]/div'


def sort_column(column_name):
    for i in range(1, 18):
        xpath_2 = ']/td[2]/div'
        xpath_full = SORT_COLUMN_LOCATOR_COMMON + str(i) + column_name
        column_data = driver.find_element(By.XPATH, xpath_full).text
        column_data_list.append(column_data)

    print(column_data_list)
    print('\n')
    print(sorted(column_data_list))


sort_column(SORT_FIRST_NAME_COLUMN)


'''
First Name
'//*[@id="PatientList"]/tbody/tr[1]/td[2]/div'
'//*[@id="PatientList"]/tbody/tr[2]/td[2]/div'
'//*[@id="PatientList"]/tbody/tr[3]/td[2]/div'

Last Name
//*[@id="PatientList"]/tbody/tr[1]/td[1]/div
//*[@id="PatientList"]/tbody/tr[2]/td[1]/div
//*[@id="PatientList"]/tbody/tr[3]/td[1]/div
'''

