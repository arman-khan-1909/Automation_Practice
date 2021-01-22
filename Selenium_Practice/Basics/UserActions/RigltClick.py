from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

'''
We will right click to use some website option not browser functions like refresh, save image etc
We will use method context_click method
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
#  driver.get("https://www.jqueryscript.net/demo/Custom-Right-Click-Context-Menu-Plugin-jQuery-contextMenu/")
driver.implicitly_wait(10)
click_box = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span')
action_chain = ActionChains(driver)
action_chain.context_click(click_box).perform()
time.sleep(3)
options = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')
for e in options:
    if e.text == "Copy":
        e.click()
        break

