from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities



class AutothonControls:
    def __init__(self, driver):
        self.driver = driver

    sign_in = (By.XPATH,"//span[text()='Sign in']")
    username = (By.XPATH,"//input[@autocomplete='username']")
    password = (By.XPATH,"//input[@autocomplete='current-password']")
    next = (By.XPATH,"//span[text()='Next']")
    login_button = (By.XPATH,"//span[text()='Log in']")
    post = (By.XPATH,"//h1[text()='Conversation']/parent::section//article/div")

    
    def get_sign_in(self):
        return self.driver.find_element(*AutothonControls.sign_in)
    def get_username(self):
        return self.driver.find_element(*AutothonControls.username)
    def get_password(self):
        return self.driver.find_element(*AutothonControls.password)
    def get_next(self):
        return self.driver.find_element(*AutothonControls.next)
    def get_login_button(self):
        return self.driver.find_element(*AutothonControls.login_button)
    def get_post(self):
        return self.driver.find_element(*AutothonControls.post)
    