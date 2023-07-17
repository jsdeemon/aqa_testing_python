from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

from royale.pages.cards_page import CardsPage

def test_ice_spirit_is_displayed():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    # 1. go to statsroyale.com 
    driver.get("https://statsroyale.com")
    time.sleep(5)
    # 2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
        # Put in a console of Chrome: on page https://statsroyale.com/cards
        #  $("[href*='Ice+Spirit']")
    # 3. asserthe spirit is displayed 

    cards_page = CardsPage(driver)
    assert cards_page.goto().map.ice_spirit_card.is_displayed
    

    # ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    # assert ice_spirit_card.is_displayed

    #Lava Golem 
    # $("[href*='Ice+Spirit']")
    lava_golem_card = driver.find_element(By.CSS_SELECTOR, "[href*='Lava+Golem']")
    assert lava_golem_card.is_displayed 

    # common-cards
    common_checkbox = driver.find_element(By.ID, 'common-cards')
    if common_checkbox.is_selected():
        common_checkbox.click()
        assert not ice_spirit_card.is_displayed


def test_ice_spirit_details_displayed():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.get("https://statsroyale.com")
    time.sleep(5)
    # 2. go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    driver.find_element(By.CSS_SELECTOR, "[href='Ice+Spirit']").click()

    
    card_name = driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text 
    # $("[class*='card__rarity']")
    split = driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']").text.split(" , ")

    card_type = split[0]
    card_arena = split[1]

    card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']").text.split("\n")[1]

    assert card_name == 'Ice Spirit'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'
