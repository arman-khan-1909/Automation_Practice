from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
'''
Can Be used for Non select dropdowns like Jquery dropdown, Angular, React, Bootstrap
To select multiple values we can call function multiple time that is not efficient
Instead of passing single value we can give array of values to to selected
The generic function will work for all single, multiple value, all values selection
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.implicitly_wait(20)


def select_choices(drop_down_list, list_of_values_to_select):
    if not list_of_values_to_select[0] == 'all':
        for e in drop_down_list:
            for i in range(len(list_of_values_to_select)):
                if e.text == list_of_values_to_select[i]:
                    e.click()
                    break
    else:
        try:
            for e in drop_down_list:
                e.click()
        except Exception as e:
            print(e)


driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(2)
drop_down = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
values_to_select = ['all']
select_choices(drop_down, values_to_select)
