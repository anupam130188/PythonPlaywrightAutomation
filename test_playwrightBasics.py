from playwright.sync_api import Page,Playwright

def test_playwrightBasics(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://google.com/")
    

def test_pagefixtureexecutionShortcut(page: Page):
    page.goto("http://google.com/")

def test_playwrightLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy");
    page.get_by_label("Password:").fill("Learning@830$3mK2");
    page.get_by_role("combobox").select_option("teach")
        