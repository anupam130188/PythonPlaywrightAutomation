from playwright.sync_api import Page

class GooglePage:
    """
    Page Object for Google Search.
    """
    def __init__(self, page: Page):
        self.page = page
        self._search_box = page.locator("[name='q']")

    def navigate(self):
        self.page.goto("https://www.google.com/")

    def search_for(self, query: str):
        self._search_box.fill(query)
        self._search_box.press("Enter")

    def click_first_result(self, text_filter: str):
        # Locate the first H3 that contains the specific text
        first_link = self.page.locator("h3").filter(has_text=text_filter).first
        first_link.click()
