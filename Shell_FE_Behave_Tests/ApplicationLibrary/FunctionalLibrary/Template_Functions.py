import time, os
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.Template_Controls import TemplateControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities
from Shell_FE_Selenium_Core.Utilities.FileUtilities import FileUtilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TemplateFunctions:

    def __init__(self):
        self.autoControls = TemplateControls(SeleniumBase.driver)
        self.article_details = []
        self.base_url = "http://ec2-54-254-162-245.ap-southeast-1.compute.amazonaws.com:9000/items/"
        self.team_name = "Shell India - 1"

    def navigate_to_x(self):
        BrowserUtilities.maximize_window()
        BrowserUtilities.navigate_to_url(SeleniumBase.url)
       
    def click_on_sign_in_button(self):
        WaitUtilities.wait_for_element_to_be_visible(self.autoControls.signin_button, 120)
        SeleniumUtilities.click_element(self.autoControls.get_signin_button())
        time.sleep(10)
       
    def enter_username_and_click_next(self):
        credentials = FileUtilities.read_json_file_as_dictionary("TwitterCredentials/TwitterCredentials.json")
        SeleniumUtilities.send_text(self.autoControls.get_username_input_field(), credentials["username"])
        time.sleep(10)
        # BrowserUtilities.log.info("Fetching username from environment variable")
        # BrowserUtilities.log.info(f"Username fetched from environment variable is: {os.environ.get('TWITTER_USERNAME')}")
        # SeleniumUtilities.send_text(self.autoControls.get_username_input_field(), os.environ.get("TWITTER_USERNAME").strip())
        SeleniumUtilities.click_element(self.autoControls.get_next_button())
        time.sleep(10)
    
    def enter_password_and_click_log_in(self):
        try:
            credentials = FileUtilities.read_json_file_as_dictionary("TwitterCredentials/TwitterCredentials.json")
            SeleniumUtilities.send_text(self.autoControls.get_password_input_field(), credentials["password"])
            time.sleep(10)
            # BrowserUtilities.log.info("Fetching password from environment variable")
            # BrowserUtilities.log.info(f"Password fetched from environment variable is: {os.environ.get('TWITTER_PASSWORD')}")
            # SeleniumUtilities.send_text(self.autoControls.get_password_input_field(), os.environ.get("TWITTER_PASSWORD").strip())
            SeleniumUtilities.click_element(self.autoControls.get_login_button())
            time.sleep(10)
            WaitUtilities.wait_for_url_to_match_value("https://x.com/home", 60)
            time.sleep(10)
        except Exception as e:
            LoggingUtilities.log_error(f"An error occurred while logging in: {e}")
            raise e

    def make_posts_and_verify_success(self):
        tweet_inputs = FileUtilities.read_json_file_as_dictionary("Tweets.json")
        WaitUtilities.wait_for_element_to_be_visible(self.autoControls.tweet_compose_textarea, 120)
        for tweet in tweet_inputs["tweets"]:
            SeleniumUtilities.send_text(self.autoControls.get_tweet_compose_textarea(), tweet)
            SeleniumUtilities.click_element(self.autoControls.get_post_button())
            time.sleep(5)
        
    def search_three_posts_and_verify_results(self):
        SeleniumUtilities.click_element(self.autoControls.get_search_button())
        WaitUtilities.wait_for_element_to_be_visible(self.autoControls.search_input_field, 60)
        SeleniumUtilities.send_text(self.autoControls.get_search_input_field(), "sign_revlis15sep")
        SeleniumUtilities.double_click(self.autoControls.get_search_result_button())

    def take_screenshot_of_posts_and_save_locally(self):
        WaitUtilities.wait_for_element_to_be_visible(self.autoControls.tweet, 60)
        self.autoControls.get_tweet().screenshot("tweet_textarea.png")