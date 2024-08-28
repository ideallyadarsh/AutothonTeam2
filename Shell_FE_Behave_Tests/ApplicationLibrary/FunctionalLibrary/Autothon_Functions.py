import time
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.Autothon_Controls import AutothonControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from Shell_FE_Requests_Core.Utilities.AssertionUtilities import AssertionUtilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class AutothonFunctions:

    def __init__(self):
        self.autoControls = AutothonControls(SeleniumBase.driver)
        self.article_details = []
        self.base_url = "http://ec2-54-254-162-245.ap-southeast-1.compute.amazonaws.com:9000/items/"
        self.team_name = "Shell India - 1"

    def navigate_to_indian_express(self):
        BrowserUtilities.maximize_window()
        SeleniumBase.driver.get("https://indianexpress.com/")
       
    def click_on_politics(self):
        WaitUtilities.wait_for_element_to_be_visible(self.autoControls.indian_express_politics, 120)
        BrowserUtilities.take_screenshot('Indian Express Home Page')
        SeleniumUtilities.is_element_displayed(self.autoControls.get_indian_express_logo())
        SeleniumUtilities.click_element(self.autoControls.get_indian_express_politics())
        BrowserUtilities.switch_to_child_window()
       
    def click_on_carousel(self):
        news_link = []
        for i in range(1, 4):
            news_link.append(SeleniumUtilities.get_attribute(self.autoControls.get_carousel("carousel",str(i)), 'href'))
            
        for link in news_link:
            BrowserUtilities.navigate_to_url(link)
            # time.sleep(5)
            WaitUtilities.wait_for_element_to_be_visible(self.autoControls.indian_express_headline, 120)
            SeleniumUtilities.scroll_to_element_by_actions(self.autoControls.get_indian_express_headline())
            headline = SeleniumUtilities.get_text(self.autoControls.get_indian_express_headline())        
            date = SeleniumUtilities.get_text(self.autoControls.get_indian_express_posted_date())
            self.article_details.append([link,headline,date])
            BrowserUtilities.take_screenshot(headline)
        SeleniumUtilities.log.info(self.article_details)
    
    def post_news_articles_details(self, article_headline, aricle_url, article_publish_date, team_name):
        headers = {     
            'Content-Type': 'application/json'  
        }
        data = {
        "name": article_headline,
        "description": aricle_url,
        "price": int(article_publish_date.split(" ")[0].replace("-", "")),
        "item_type": team_name,
        }
        SeleniumUtilities.log.info(f"News article details: \nHeadline: {article_headline} \nURL: {aricle_url} \nPublish Date: {article_publish_date} \n Team Name: {team_name}")
        RequestsBase.post_request(url = self.base_url, headers= headers, body_json= data)

    def validate_news_articles_details(self, article_headline, aricle_url, article_publish_date, team_name, id):
        RequestsBase.get_request(url = self.base_url + str(id))
        if RequestsBase.response_status_code(RequestsBase.response) != 200:
            
            SeleniumUtilities.log.error(f"Retrieval of News Article with ID: {id} failed \nResponse received: {RequestsBase.response_body_as_string(RequestsBase.response)}")
        SeleniumUtilities.log.info(f"Successful Retrieval of News Article with ID: {id} \nResponse received: {RequestsBase.response_body_as_string(RequestsBase.response)}")
        response = RequestsBase.response_body_as_dictionary(RequestsBase.response)

        if response.get("name") == article_headline and response.get("description") == aricle_url and int(response.get("price")) == int(article_publish_date.split(" ")[0].replace("-", "")) and response.get("item_type") == team_name:
            SeleniumUtilities.log.info(f"Successful validation for News Article with ID: {id}")
        else:
            SeleniumUtilities.log.error(f"Validation failed for News Article with ID: {id} \nResponse received: {RequestsBase.response_body_as_string(RequestsBase.response)}")
    
    def post_and_validate_article_details(self):
        for i in range(len(self.article_details)):
            SeleniumUtilities.log.info('-'*60)
            self.post_news_articles_details(self.article_details[i][0],self.article_details[i][1],self.article_details[i][2], self.team_name)
            # response = API.post(self.article_details[i][0],self.article_details[i][1],self.article_details[i][2])
            if RequestsBase.response_status_code(RequestsBase.response) != 200:
                SeleniumUtilities.log.error(f"News Article was not posted \nResponse received: {RequestsBase.response_body_as_string(RequestsBase.response)}")   
            
            id = RequestsBase.response_body_as_dictionary(RequestsBase.response).get("id")
            SeleniumUtilities.log.info(f"News Article posted successfully with id {id}...")
            self.validate_news_articles_details(self.article_details[i][0],self.article_details[i][1],self.article_details[i][2], self.team_name, id)

 