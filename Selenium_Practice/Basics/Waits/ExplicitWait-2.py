import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
'''
1. After clicking login button a alert will come in rediff mail, we need to click ok
2. Alert takes some time to visible. So explicitly we need to tell Selenium to wait for that Alert to be present
3. Then get the message and click ok
4. alert_is_present() -> Checks and Switches to Alert also, returns reference of same alert
5. See JS_Alert_PopUp script, we used time.sleep there 
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element_by_name("proceed").click()
wait = WebDriverWait(driver, 20)
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()
