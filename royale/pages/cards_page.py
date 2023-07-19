from royale.pages.base.pagebase import PageBase
from selenium.webdriver.common.by import By 

class CardsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardsPageMap(driver) 
    
    def goto(self):
        self.headernav.goto_cards_page()
        return self
    
    def get_card_by_name(self, card_name: str):
        if ' ' in card_name:
            card_name = card_name.replace(' ', '+')
        return self.map.card(card_name)
       


class CardsPageMap:

    def __init__(self, driver):
        self._driver = driver

    # @property
    # def ice_spirit_card(self):
    #     return self._driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    
    def card(self, card_name):
        return self._driver.find_element(By.CSS_SELECTOR, "[href*='{card_name}']")