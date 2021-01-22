import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
'''
1. EC methods which accepts locator means we need ot provide give a locator technique in it like By.ID
2. Methods which accept element means we need to locate element first and then pass that in element
'''
driver = webdriver.Edge(executable_path="G:\\Selenium\\others\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window()
driver.get("https://www.icicidirect.com/charting/advance/AffleIndiaLtd-73060-nse")
wait = WebDriverWait(driver, 20)
element = driver.find_element(By.XPATH, '//*[@id="main-body"]/div[2]')
wait.until(ec.visibility_of(element))
driver.execute_script('window.scrollTo(0,300);')
# time.sleep(10)  # Works fine if we use this
six_month = wait.until(ec.visibility_of_element_located((By.ID, '6month')))
'''
selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: 
Element <div class="range-buttons range-buttons-advanced" id="6month">...</div> is not clickable at point (265, 580). 
Other element would receive the click: <div class="loader full_page_loader black_overlay">...</div>

Solution
1. It is a problem with Chrome, Working Fine in Edge Browser
2. Use ActionsChains and mouse hover to that element first then click
'''