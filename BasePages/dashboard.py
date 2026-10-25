from utils.UI_Utils import UIUtils
class Dashboard (UIUtils):
    
    def __init__(self, page):
        self.page=page
        self.productslist= page.locator("app-card");
    
    def wait_for_url(self,value):
        self.page.wait_for_url("**/"+value)
    
    def click_checkout(self):
        self.page.get_by_text("Checkout").click();
    
    def click_element_on_UI(self,locator, product):
        self.element_visibility_check(product)
        self.click_element(locator,product)
    
    # def select_product(self,product):
    #     cards = self.page.locator("app-card")
    #     self.click_element(cards)
    #     # for index in range(cards.count()):
    #     #     card = cards.nth(index)
    #     #     title = card.locator(".card-title").inner_text().strip()
    #     #     print("title :", title)
    #     #     if title == product:
    #     #         card.locator(".card-footer .btn").click()
    #     #         break
    #     self.page.get_by_text("Checkout").click();