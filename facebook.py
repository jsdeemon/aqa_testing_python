from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time  

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 
driver.get("https://facebook.com")
driver.maximize_window()

loginBtn = driver.find_element(By.NAME, 'login')

time.sleep(3)
print(driver.title)
print(loginBtn)
driver.close()