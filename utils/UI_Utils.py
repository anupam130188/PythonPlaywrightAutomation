from playwright.sync_api import Locator, expect
class UIUtils:

    def __init__(self, page):
        self.page=page

    def element_visibility_check(self,product):
        expect(self.page.get_by_text(product)).to_be_visible()

    # def element_click(self,page,locator):
    #         expect(self.page.get_by_text(product)).to_be_visible()

    def click_element(self,loc, product):
        for index in range(loc.count()):
            card = loc.nth(index)
            title = card.locator(".card-title").inner_text().strip()
            print("title :", title)
            if title == product:
                card.locator(".card-footer .btn").click()
                break

    def get_text(self, loc):
        return loc.text_content();

    def element_click_by_text(self, loc):
            loc.click();
