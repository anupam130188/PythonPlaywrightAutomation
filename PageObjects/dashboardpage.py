from BasePages.dashboard import Dashboard
from PageObjects.checkoutpage import CheckoutPage

class DashboardPage(Dashboard):
    
    def __init__(self,page):
        self.page=page
        super().__init__(page)
    
    def select_product(self,product):
      #  cards = self.productslist;
        self.click_element_on_UI(self.productslist, product)
        self.click_checkout();
        checkoutPage = CheckoutPage(self.page);
        return checkoutPage;