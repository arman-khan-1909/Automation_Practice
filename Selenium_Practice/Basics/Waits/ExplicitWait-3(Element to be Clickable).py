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
driver.get("https://www.goibibo.com/gostays/find-hotels-in-Goa/8717279093827200968/8717279093827200968/%7B%22ci%22"
           ":%2220210106%22,%22co%22:%2220210107%22,%22r%22:%221-2-0%22%7D/?{%22filter%22:{%22tag%22:%22goStays%22,"
           "%22fc%22:0}}&sec=dom&cc=IN")
driver.execute_script('window.scrollTo(0,300)')
wait = WebDriverWait(driver, 10)
element = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'jUKYxg')))
element.click()
