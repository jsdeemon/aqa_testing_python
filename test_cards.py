from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

from royale.pages.cards_page import CardsPage
from royale.pages.card_details_page import CardDetailsPage
from royale.services import card_service

import pytest

cards = card_service.get_all_cards()

@pytest.mark.parametrize('api_card', cards)
def test_card_is_displayed(api_card):
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
    # driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
        # Put in a console of Chrome: on page https://statsroyale.com/cards
        #  $("[href*='Ice+Spirit']")
    # 3. asserthe spirit is displayed 

    cards_page = CardsPage(driver).goto()
    ice_spirit = cards_page.get_card_by_name(api_card.name)
    assert ice_spirit.is_displayed()
    

    # ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    # assert ice_spirit_card.is_displayed

    #Lava Golem 
    # $("[href*='Ice+Spirit']")
    # lava_golem_card = driver.find_element(By.CSS_SELECTOR, "[href*='Lava+Golem']")
    # assert lava_golem_card.is_displayed 

    lava_golem_card = cards_page.get_card_by_name("Lava Golem")
    assert lava_golem_card.is_displayed()

    # common-cards
    common_checkbox = driver.find_element(By.ID, 'common-cards')
    if common_checkbox.is_selected():
        common_checkbox.click()
        assert not ice_spirit.is_displayed


@pytest.mark.parametrize('api_card', cards)
def test_card_details_displayed(api_card):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.get("https://statsroyale.com") 

    # 2. go to cards page
    # driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    # driver.find_element(By.CSS_SELECTOR, "[href='Ice+Spirit']").click()
    CardsPage(driver).goto().get_card_by_name(api_card.name).click()

    card = CardDetailsPage(driver).get_base_card()

    assert card.name == api_card.name
    assert card.type == api_card.type
    assert card.arena == api_card.arena
    assert card.rarity == api_card.rarity
    # card_name = details_page.map.card_name.text 
    # split = details_page.map.card_category.text.split(' , ')
    # card_type = split[0]
    # card_arena = split[1]
    # card_rarity = details_page.map.card_rarity.text.split("\n")[1]

    # card_name = driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text 
    # # $("[class*='card__rarity']")
    # split = driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']").text.split(" , ")

    # card_type = split[0]
    # card_arena = split[1]

   

    # card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']").text.split("\n")[1]

    # assert card_name == 'Ice Spirit'
    # assert card_type == 'Troop'
    # assert card_arena == 'Arena 8'
    # assert card_rarity == 'Common'



# def test_mirror_details_displayed():
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     driver.maximize_window()

#     driver.get("https://statsroyale.com") 

#     time.sleep(5)
#     # 2. go to cards page
#     CardsPage(driver).goto().get_card_by_name("Mirror").click()

#     card = CardDetailsPage(driver).get_base_card()

#     assert card.name == 'Mirror'
#     assert card.type == 'Spell'
#     assert card.arena == 12
#     assert card.rarity == 'Epic'