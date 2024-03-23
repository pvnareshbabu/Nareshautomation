
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path='C://Users//91900//Documents//Python_data//chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get(url='https://googlechromelabs.github.io/chrome-for-testing/#stable')
driver.maximize_window()
time.sleep(10)

