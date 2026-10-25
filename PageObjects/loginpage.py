from BasePages.login import Login
from PageObjects.dashboardpage import DashboardPage
class LoginPage(Login):
    
    def __init__(self, page):
        self.page=page
        super().__init__(page)
    
    
    def navigate_to_homepage(self,userEmail,userPassword):
       # self.page.goto(environment_config["url"])
        self.enter_username(userEmail);
        self.enter_password(userPassword);
        self.select_role_dropdown();
        self.agree_terms_click();
        self.sign_in_btnClick();
        dashboardPage = DashboardPage(self.page)
        return dashboardPage;
        #dashboardPage = DashboardPage(page); #moved this instance to Login as creating instance after login is happening
    
    def navigate_to_homePage_with_invalid_password(self,userEmail,userPassword):
           # self.page.goto(environment_config["url"])
            self.enter_username(userEmail);
            self.enter_password(userPassword);
            self.select_role_dropdown();
            self.agree_terms_click();
            self.sign_in_btnClick();
            self.get_error_text();
            
    def navigate_to_homePage_with_invalid_username(self,userEmail,userPassword):
               # self.page.goto(environment_config["url"])
                self.enter_username(userEmail);
                self.enter_password(userPassword);
                self.select_role_dropdown();
                self.agree_terms_click();
                self.sign_in_btnClick();
                self.get_error_text();
                
            
            
    
            
            