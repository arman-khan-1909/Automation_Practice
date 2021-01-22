import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
'''
We will learn how to Switch to various elements like JS alert Pop up, Authentication popup, Frames
Alerts made by JS alert method are not Web Elements and hence we cannot inspect and locate them
We will use Webdriver Property switch_to.alert
1. alert.accept() -> clicks ok
2. alert.dismiss() -> cancel the popup
3. alert.sendkeys() -> if we need enter something in alert box
4. After we perform action on pop up we again need to comeback to our main content 
5. By driver.switch_to.default_content() 
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element_by_name("proceed").click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.accept()
# alert.dismiss()
driver.switch_to.default_content()
