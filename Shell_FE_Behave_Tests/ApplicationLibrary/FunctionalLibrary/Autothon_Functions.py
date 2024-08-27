import time
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.Autothon_Controls import AutothonControls
from Shell_FE_Behave_Tests.ApplicationLibrary.ControlLibrary.Linkedin_controls import LinkedinControls
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.BrowserUtilities import BrowserUtilities
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities
from Shell_FE_Selenium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
from requests_oauthlib import OAuth1Session
import random,requests,json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def wait_for_page_to_load(driver, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )

def scroll_into_center(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

class AutothonFunctions:

    def __init__(self):
        self.autoControls = AutothonControls(SeleniumBase.driver)
        self.linkControls = LinkedinControls(SeleniumBase.driver)

    def navigate_to_twitter(self):
        BrowserUtilities.maximize_window()
        SeleniumBase.driver.get("https://www.x.com")
        time.sleep(5)
        SeleniumUtilities.click_element(self.autoControls.get_remove_tnc())
        scroll_into_center(SeleniumBase.driver, self.autoControls.get_sign_in())
        SeleniumUtilities.click_element(self.autoControls.get_sign_in())

        SeleniumUtilities.send_text(self.autoControls.get_username(),"adarshmeledam@gmail.com")
        SeleniumUtilities.click_element(self.autoControls.get_next())
        try:
            SeleniumUtilities.is_element_displayed(self.autoControls.get_enter_username())
            SeleniumUtilities.send_text(self.autoControls.get_enter_username(),"adarshmele37994")
            SeleniumUtilities.click_element(self.autoControls.get_next())
        except:
            pass
        SeleniumUtilities.send_text(self.autoControls.get_password(),"Meledam@526902")
        SeleniumUtilities.click_element(self.autoControls.get_login_button())
        wait_for_page_to_load(SeleniumBase.driver)
        time.sleep(5)
        
    
    def navigate_to_linkedin(self):
        BrowserUtilities.maximize_window()
        SeleniumBase.driver.get("https://www.linkedin.com")
        WaitUtilities.wait_for_element_to_be_clickable(self.linkControls.sign_in, 60)
        SeleniumUtilities.click_element(self.linkControls.get_sign_in())
        SeleniumUtilities.send_text(self.linkControls.get_username(),"parthvenkatesh@zohomail.in")
        SeleniumUtilities.send_text(self.linkControls.get_password(),"Par@98124")
        SeleniumUtilities.click_element(self.linkControls.get_login_button())
        time.sleep(5)


    
    def call_twitter_api(self):
        consumer_key ='uNfKZWHed3IhbynWI9bjloKW8' 
        consumer_secret ='JxA7diUrryFmBl5OZDsUHVa2PnL4SVgWrRROLqBHz7D9PS5ne7' 
        access_token ='1825070392123199488-2pZ3kHu3b8aJAvLIRkcrJSdBDgXdwI' 
        token_secret ='qHC5NYFJuWixtGiFBRGmX2PfVamMPi61FTpUfXcb5x7DG' 
        oauth = OAuth1Session( consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=token_secret ) 
        url = 'https://api.twitter.com/2/tweets' 
        headers = {     'Content-Type': 'application/json'  } 
        payload = { 'text': 'Tweet#'+ str(random.randint(100000, 999999)) +'-- Hello @parthvenkatesh!!!!!! This is a tweet from Python using OAuth 1.0a.' } 
        response = oauth.post(url, json=payload,headers=headers,verify=False) 
        SeleniumUtilities.log.info(f"Status Code: {response.status_code}") 
        SeleniumUtilities.log.info("Response JSON:", response.json())
        response_json = response.json() 
        return response_json.get('data', {}).get('id')

    def screenshot_tweet(self,tweet_id):
        url =  'https://x.com/adarshmele37994/status/' + str(tweet_id)
        BrowserUtilities.navigate_to_url(url)
        # SeleniumBase.driver.get(url)
        WaitUtilities.wait_for_element_to_be_present(self.autoControls.post,40)
        element = self.autoControls.get_post()
        sc = element.screenshot_as_png
        with open('TestData/Images/tweet.png', 'wb') as file:
            file.write(sc)

    def call_linkedin_api(self):
        url = 'https://api.linkedin.com/v2/ugcPosts'
        access_token = "AQXLe42JPfDPomL862szd5o53RFeg1j1m2vA6HQY7W8-NZrc_e0VC4ZsZOG0Wrbyq2K4YtIF6XxDhNoVuBrsSeFVeoOTbGhlP2aPWySJz4dAokIru8g_0vrCpa_e0Et2cpyJ3g4IsxYwQydTVvc_f1JQaz8Ol7GLhlwKn-jjm-cIWiGGIqGuhH_D3MpOCJgGUAF0MOwpbjvmSXG_0x9gtzAp2SGQVhQ2o0gQyvXxxc5EKBkZyHt63b0o0ZDppQaQbOzRcwzwNixP-fjoBoDPq92ps3r3JJz5b5qeageNgp0wTpwnRNAda6e35RyW8q2W_0Ev509vKLZRF0mZhcXwg17uY-Nf5w"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0'
            }
        payload = { 
            "author": "urn:li:person:llk7SeTC6i", 
            "lifecycleState": "PUBLISHED", 
            "specificContent": { 
                "com.linkedin.ugc.ShareContent": { 
                    "shareCommentary": { 
                        "text": 'LinkedIn Post#:'+ str(random.randint(100000, 999999)) +"-- Hello LinkedIn!! This is a test post from the API." 
                        },
                        "shareMediaCategory": "NONE", 
                        "media": [] 
                        } 
                    }, 
                    "visibility": { 
                        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC" 
                    } 
                }
        response = requests.post(url, headers=headers, data=json.dumps(payload),verify=False)
        post_data = response.json()
        post_id = post_data.get('id')
        SeleniumUtilities.log.info(post_id)
        return post_id
    
    def screenshot_linkedin_post(self,post_id):
        url =  'https://www.linkedin.com/feed/update/' + str(post_id)
        # SeleniumBase.driver.get(url)
        BrowserUtilities.navigate_to_url(url)
        WaitUtilities.wait_for_element_to_be_present(self.linkControls.post,40)
        element = self.linkControls.get_post()
        sc = element.screenshot_as_png
        with open('TestData/Images/linkedin.png', 'wb') as file:
            file.write(sc)

    def navigate_to_facebook(self):
        BrowserUtilities.maximize_window()
        SeleniumBase.driver.get("https://www.facebook.com")
        # time.sleep(5)
        # SeleniumUtilities.send_text(self.autoControls.get_user(), 'abc')
        WaitUtilities.wait_for_element_to_be_visible((By.ID,'email'), 60)
        SeleniumUtilities.send_text(SeleniumBase.driver.find_element(By.ID,'email'),"adarshmeledam@gmail.com")
        SeleniumUtilities.send_text(SeleniumBase.driver.find_element(By.ID,'pass'),"ada7338928530")
        SeleniumUtilities.click_element(SeleniumBase.driver.find_element(By.ID('loginbutton')))
        # time.sleep(10)

 