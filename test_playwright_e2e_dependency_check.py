from playwright.sync_api import Playwright, expect
import pytest
from PageObjects.loginpage import LoginPage
# from PageObjects.dashboardpage import DashboardPage
# from PageObjects.checkoutpage import CheckoutPage

# def test_e2e_web_api(playwright: Playwright, environment_config):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto(environment_config["url"])
# changed the code to handle the browser from fixture instead
# of hardcoding it in script via context creation
#def test_e2e_web_api(page, environment_config, screenshot_dir, product):
#for parallel execution install xdist : pip install pytest-xdist
# after installation syntax : pytest -n 3(here 3 tells the no of workers in parallel to rn tests)
#@pytest.mark.smoke

@pytest.mark.dependency(name="login_success")
def test_login_check(browserInstance, environment_config):
    browserInstance.goto(environment_config["url"])
    loginPage = LoginPage(browserInstance);
    dashboardPage = loginPage.navigate_to_homepage(environment_config["email"],environment_config["password"])
    #page.screenshot(path=screenshot_dir / "login_Page.png")
    #dashboardPage = DashboardPage(page); #move this instance to Login as t is happening after login
    dashboardPage.wait_for_url("shop")

@pytest.mark.dependency(depends=["login_success"])
def test_e2e_web_api(browserInstance, environment_config,  product):
    browserInstance.goto(environment_config["url"])
    loginPage = LoginPage(browserInstance);
    dashboardPage = loginPage.navigate_to_homepage(environment_config["email"],environment_config["password"])
    #page.screenshot(path=screenshot_dir / "login_Page.png")
    #dashboardPage = DashboardPage(page); #move this instance to Login as t is happening after login
    dashboardPage.wait_for_url("shop")
    checkoutPage= dashboardPage.select_product(product)
    #checkoutPage = CheckoutPage(page);
    expect(checkoutPage.product_count).to_have_count(1)
    checkOutVal=checkoutPage.get_product_text();
    print("checkOutVal :", checkOutVal)
    assert checkOutVal.strip() == product
    checkoutPage.checkout_product()
   
#@pytest.mark.dependency(depends=["login_success"])
def test_e2e_invalid_password(page, environment_config):
    page.goto(environment_config["url"])
    loginPage = LoginPage(page);
    loginPage.navigate_to_homePage_with_invalid_password(environment_config["email"],"test@123")

# #@pytest.mark.skip
#@pytest.mark.dependency(depends=["login_success"])
def test_e2e_invalid_email(page, environment_config):
    page.goto(environment_config["url"])
    loginPage = LoginPage(page);
    loginPage.navigate_to_homePage_with_invalid_username("test@123",environment_config["password"])
    
    

    
        
        