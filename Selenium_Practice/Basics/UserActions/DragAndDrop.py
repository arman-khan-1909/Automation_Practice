from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

'''
Check Frames Example
Drag and drop is click and hold move to a location and release.
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
driver.implicitly_wait(10)
source = driver.find_element(By.XPATH, '//*[@id="todrag"]/span[2]')
target = driver.find_element(By.ID, 'mydropzone')
action_chains = ActionChains(driver)
time.sleep(2)
#  action_chains.drag_and_drop(source, target1).perform()
action_chains.click_and_hold(source).move_to_element(target).release(source).perform()
