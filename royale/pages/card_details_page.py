from selenium.webdriver.common.by import By 
from royale.pages.cards_page import PageBase
from royale.models.card import Card 

class CardDetailsPage(PageBase):
    def __init__(self, driver):
        super.__init__(driver)
        self.map =CardDetailsPageMap

    def get_card_type_and_arena(self):
        type_and_arena = self.map.card_category.text.split(' , ')
        card_type = type_and_arena[0]
        card_arena = type_and_arena[1].split(' ')[-1]
        return card_type, int(card_arena)
    
    def get_base_card(self):
        type_and_arena = self.get_card_type_and_arena()
        return Card(
            name=self.map.card_name.text,
            type=type_and_arena[0],
            arena=type_and_arena[1],
            rarity=self.map.card_rarity.text.split("\n")[-1]
        )

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