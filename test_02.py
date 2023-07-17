from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

def test_google_search():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 1. go to google.com 
    driver.get("https://google.com")
    
    # 2. type in search "puppies"
    driver.find_element(By.NAME, 'q').send_keys('puppies')
    # 3. submit a search 
    driver.find_element(By.NAME, 'btnK').submit()
    
    # 4. assert we got a page with puppies  
    assert 'puppies' in driver.title