from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service('C:\Driver\chromedriver')
driver=webdriver.Chrome(service=s)
driver.get('https://v2apptest.shippigo.in/login')
driver.implicitly_wait(3)
driver.find_element(By.,"//*[@id='mat-input-7']")
# element.send_keys('aditya')