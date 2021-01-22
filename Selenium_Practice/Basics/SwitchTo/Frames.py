import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
'''
Browser -> Page -> Frame -> Element
1. Frame is a part of page but we cannot access elements of a Frame directly, though it is a Web element
2. driver.switch_to.frame('name or id etc' or 'index')
3. After performing operation we need to comeback to main content driver.switch_to.default_content()
4. If there are child frames, can come back to parent frame also driver.switch_to.parent_frame() 
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/droppable/")
frame_element = driver.find_element_by_class_name("demo-frame")
driver.switch_to.frame(frame_element)
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
action_chains = ActionChains(driver)
time.sleep(3)
action_chains.drag_and_drop(source, target).perform()
driver.switch_to.default_content()
driver.switch_to.parent_frame()

