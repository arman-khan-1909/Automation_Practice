from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.facebook.com")
email_element = driver.find_element_by_name("email")
pass_element = driver.find_element_by_name("pass")
print(email_element.is_displayed())  # To check if email displayed or not
print(email_element.is_enabled())  # To check if password enabled or not
driver.find_element_by_link_text("Create New Account").click()
# driver.find_element_by_xpath("//div[@id='u_5_n']/span[@id='u_5_o']/span[2]/label").click()


