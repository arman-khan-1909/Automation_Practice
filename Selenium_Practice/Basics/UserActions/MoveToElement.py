from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Move to Element, Mouse hover actions like some options coming on mouse hover, # Right Click action, # Drag and Drop
# We will use class ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://spicejet.com")
driver.implicitly_wait(20)
'''
Move to element
Hover on Login/SignUp -> Spice Club Members -> Member Login(click here)
'''
action_chains = ActionChains(driver)
login_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
action_chains.move_to_element(login_ele).perform()  # we need to add perform end
spiceclub_ele = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
action_chains.move_to_element(spiceclub_ele).perform()
member_login_ele = driver.find_element(By.LINK_TEXT, 'Member Login')
member_login_ele.click()
