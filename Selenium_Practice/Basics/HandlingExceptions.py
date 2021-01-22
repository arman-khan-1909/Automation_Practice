from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
# driver.implicitly_wait(1)
driver.get('http://www.amazon.in')
try:
    driver.find_element(By.ID, "xyz").click()
    var = 1 / 0  # Any generic exception for example
except WebDriverException:
    print("Connection is terminated")
except NoSuchElementException as e:
    # In this except we want to handle only Nosuchelement exception
    print("The the element you are trying to locate does not exist")
except Exception:
    # Here we will handle any other generic exception
    print("Sorry Something went wrong")
else:
    print("No exception occurred")
