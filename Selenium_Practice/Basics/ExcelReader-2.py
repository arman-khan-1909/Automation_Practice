import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
'''
We will fill Orange HRM free trial from by fetching data from excel file
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
sheet = xlrd.open_workbook('OrangeHR.xls').sheet_by_name('Sheet1')
time.sleep(2)
