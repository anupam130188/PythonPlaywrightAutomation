from utils.UI_Utils import UIUtils
from playwright.sync_api import Page, expect

class Checkout(UIUtils):
    
    def __init__(self,page):
        self.page=page;
        self.product_text =page.locator("h4.media-heading");
        self.product_checkout=page.get_by_text("Checkout");
        self.product_count=page.locator("input#exampleInputEmail1");
    
    def get_product_text(self):
        return self.get_text(self.product_text);
    
    def checkout_product(self):
        self.element_click_by_text(self.product_checkout);
        