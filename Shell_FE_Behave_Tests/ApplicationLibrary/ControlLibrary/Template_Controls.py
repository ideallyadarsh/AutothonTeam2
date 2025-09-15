from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities

class TemplateControls:
    def __init__(self, driver):
        self.driver = driver

    signin_button = (By.XPATH, "//a[@href='/login']")
    username_input_field = (By.XPATH, "//input[@autocomplete='username']")
    next_button = (By.XPATH, "//span[text()='Next']//ancestor::button")
    password_input_field = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//span[text()='Log in']//ancestor::button[1]")
    tweet_compose_textarea = (By.XPATH, "//div[@aria-label='Post text']")
    post_button = (By.XPATH, "//span[text()='Post']//ancestor::button")
    search_button = (By.XPATH, "//a[@href='/explore']")
    search_input_field = (By.XPATH, "//input[@aria-label='Search query']")
    search_result_button = (By.XPATH, "//span[contains(text(), 'Search for')]//ancestor::button")
    tweet = (By.XPATH, "//article[@data-testid='tweet'][1]")

    def get_signin_button(self):
        return self.driver.find_element(*TemplateControls.signin_button)
    
    def get_username_input_field(self):
        return self.driver.find_element(*TemplateControls.username_input_field)
    
    def get_next_button(self):
        return self.driver.find_element(*TemplateControls.next_button)

    def get_password_input_field(self):
        return self.driver.find_element(*TemplateControls.password_input_field)

    def get_login_button(self):
        return self.driver.find_element(*TemplateControls.login_button)
    
    def get_tweet_compose_textarea(self):
        return self.driver.find_element(*TemplateControls.tweet_compose_textarea)
    
    def get_post_button(self):  
        return self.driver.find_element(*TemplateControls.post_button)
    
    def get_search_button(self):
        return self.driver.find_element(*TemplateControls.search_button)
    
    def get_search_input_field(self):
        return self.driver.find_element(*TemplateControls.search_input_field)

    def get_search_result_button(self):
        return self.driver.find_element(*TemplateControls.search_result_button)

    def get_tweet(self):
        return self.driver.find_element(*TemplateControls.tweet)