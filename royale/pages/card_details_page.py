from selenium.webdriver.common.by import By 
from royale.pages.cards_page import PageBase

class CardDetailsPage(PageBase):
    def __init__(self, driver):
        super.__init__(driver)
        self.map =CardDetailsPageMap

        

class CardDetailsPageMap:
    def __init__(self, driver):
        self._driver = driver

    
    @property
    def card_name(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text 
    
    @property
    def card_category(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']")
    
    @property
    def card_rarity(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']")