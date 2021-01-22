from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

'''
1. By help of this we can run JS code in our script
2. Helpful when we cannot perform certain function using selenium like getting innerText
3. Or generate some alert, scrolling page
4  If our normal click is not working we can pass argument[0].click and web element 
5. Inner text gives text of all Web elements available on page
6. Drawing a border for any element. Suppose there is a bug so we can border it b4 taking screenshot
7. scrollToView -> on bestseller page we want to click watches link on left, this JS functions only
                    scrolls till that element is visible 
'''
driver = webdriver.Chrome(executable_path="G:\\Selenium\\others\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.in")
best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
driver.execute_script("arguments[0].click();", best_sellers)
title = driver.execute_script("return document.title;")  # Getting title by JS
print(title)
# driver.execute_script('alert("Alert By JS");')  # Generate Alert
# inner_text = driver.execute_script("document.documentElement.innerText;")
# print(inner_text)
most_gifted = driver.find_element(By.LINK_TEXT, 'Most Gifted')
driver.execute_script("arguments[0].style.border = '3px solid red'", most_gifted)
watches_link = driver.find_element(By.LINK_TEXT, 'Watches')
driver.execute_script("arguments[0].scrollIntoView(true)", watches_link)
# userAgent = driver.execute_script("return navigator.userAgent;")
# print(userAgent)  # To get types of browser
driver.execute_script("window.scrollTo(300,0);")  # -> value in first arg means scroll up
# driver.execute_script("document.getElementById('email').value='test@gmail.com'") -> Equivalent to sendkeys
