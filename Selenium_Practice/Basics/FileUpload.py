import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
'''
This is just a hack to upload file, later it can be done by sikuli, id
Inspect the choose file element and its type shud be file
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(2)
driver.find_element(By.NAME, 'file').send_keys('C:\\Users\\Arman\\Desktop\\demo.txt')
time.sleep(2)
driver.find_element(By.ID, 'file-submit').click()


