from playwright.sync_api import Playwright, expect

def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="terms").click()
    page.locator("#signInBtn").click()
    page.wait_for_url("**/shop")
    expect(page.get_by_text("iphone X")).to_be_visible()
    cards = page.locator("app-card")

    for index in range(cards.count()):
        card = cards.nth(index)
        title = card.locator(".card-title").inner_text().strip()
        print("title :", title)
        if title == "Samsung Note 8":
            card.locator(".card-footer .btn").click()
            break
    page.get_by_text("Checkout").click();
    expect(page.locator("input#exampleInputEmail1")).to_have_count(1)
    
    checkOutVal=page.locator("h4.media-heading").text_content();
    print("checkOutVal :", checkOutVal)
    assert checkOutVal.strip()=="Samsung Note 8"
    page.get_by_text("Checkout").click();
    #page.wait_for_url("**/shops");
    
        
        