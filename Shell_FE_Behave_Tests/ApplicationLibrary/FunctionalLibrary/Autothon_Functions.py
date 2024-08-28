import time
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.Autothon_Controls import AutothonControls
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.Linkedin_controls import LinkedinControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Behave_Tests.ApiLibrary.API import API
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from requests_oauthlib import OAuth1Session
import random,requests,json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AutothonFunctions:

    def __init__(self):
        self.autoControls = AutothonControls(SeleniumBase.driver)
        self.article_details = []

    def navigate_to_indian_express(self):
        BrowserUtilities.maximize_window()
        SeleniumBase.driver.get("https://indianexpress.com/")
        # WaitUtilities.wait_for_element_to_be_visible(self.autoControls.indian_express_allow_button, 120)
        # SeleniumUtilities.click_element(self.autoControls.get_indian_express_allow_button())
       
    def click_on_politics(self):
        SeleniumUtilities.click_element(self.autoControls.get_indian_express_politics())
        BrowserUtilities.switch_to_child_window()
       
    def click_on_carousel(self):
        news_link = []
        news_link.append(self.autoControls.get_carousel_1().get_attribute('href'))
        news_link.append(self.autoControls.get_carousel_2().get_attribute('href'))
        news_link.append(self.autoControls.get_carousel_3().get_attribute('href'))
        for link in news_link:
            BrowserUtilities.navigate_to_url(link)
            time.sleep(2)
            headline = SeleniumUtilities.get_text(self.autoControls.get_indian_express_headline())        
            date = SeleniumUtilities.get_text(self.autoControls.get_indian_express_posted_date())
            self.article_details.append([link,headline,date])

        SeleniumUtilities.log.info(self.article_details)
    
    def post_and_validate_article_details(self):
        for i in range(len(self.article_details)):
            SeleniumUtilities.log.info('-'*60)
            response = API.post(self.article_details[i][0],self.article_details[i][1],self.article_details[i][2])
            if response:
                SeleniumUtilities.log.info(f"News Article {i+1} posted successfully")
                validation = API.validate(self.article_details[i][0],self.article_details[i][1],self.article_details[i][2],response)
                if validation:
                    SeleniumUtilities.log.info(f"News Article {i+1} validated successfully. Id :{validation}")
                else:
                    self.log_file.error(f"News Article {i+1} not validated successfully. Id :{validation}")
                    raise AssertionError(f"News Article {i+1} not validated successfully. Id :{validation}")
            else:
                self.log_file.error(f"News Article with ID: {id} not posted successfully")
 