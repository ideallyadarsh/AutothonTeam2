from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities



class LinkedinControls:
    def __init__(self, driver):
        self.driver = driver

    sign_in = (By.XPATH,"//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']")
    username = (By.XPATH,"//input[@id='username']")
    password = (By.XPATH,"//input[@id='password']")
    login_button = (By.XPATH,"//button[@aria-label='Sign in']")
    post = (By.XPATH,"//div[@role='status']/following-sibling::div//div[@id='fie-impression-container']")

    
    def get_sign_in(self):
        return self.driver.find_element(*LinkedinControls.sign_in)
    def get_username(self):
        return self.driver.find_element(*LinkedinControls.username)
    def get_password(self):
        return self.driver.find_element(*LinkedinControls.password)
    def get_login_button(self):
        return self.driver.find_element(*LinkedinControls.login_button)
    def get_post(self):
        return self.driver.find_element(*LinkedinControls.post)
    