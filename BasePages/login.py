from playwright.sync_api import Playwright

class Login:
    
    def __init__(self, page):
        self.page=page
          
    def enter_username(self,userEmail):
        self.page.get_by_label("Username:").fill(userEmail);
        
    def enter_password(self,userPassword):
        self.page.get_by_label("Password:").fill(userPassword)

        
    def select_role_dropdown(self):
        self.page.get_by_role("combobox").select_option("teach")
    
    def agree_terms_click(self):
        self.page.get_by_role("checkbox", name="terms").click()

    def sign_in_btnClick(self):
        self.page.locator("#signInBtn").click()
            
    def get_error_text(self):
        print("print value :", self.page.locator("div.alert-danger").text_content());
        #self.page.wait_for_url("**/shops");
        
    