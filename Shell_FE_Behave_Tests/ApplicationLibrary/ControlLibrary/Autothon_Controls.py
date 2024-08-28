from selenium.webdriver.common.by import By
from Shell_FE_Selenium_Core.Utilities.SeleniumUtilities import SeleniumUtilities



class AutothonControls:
    def __init__(self, driver):
        self.driver = driver

    indian_express_allow_button = (By.XPATH, "(//button[contains(text() , 'Allow')])[1]")
    indian_express_politics = (By.XPATH, "//a[@data-ie-event-label='Politics']")
    indian_express_corousel = (By.XPATH, "//button[@id='slick-slide-control01']")
    indian_express_headline = (By.XPATH, "//h1[@itemprop = 'headline']")
    indian_express_posted_date = (By.XPATH, "//div[@class = 'ie-first-publish']/span")
    indian_express_logo = (By.XPATH, "//img[@alt='The Indian Express logo']")
    carousel_1 = (By.XPATH, "(//div[@class='slickslider-box']//a)[1]")
    carousel_2 = (By.XPATH, "(//div[@class='slickslider-box']//a)[2]")
    carousel_3 = (By.XPATH, "(//div[@class='slickslider-box']//a)[3]")
   
    def get_carousel_1(self):
        return self.driver.find_element(*AutothonControls.carousel_1)
    def get_carousel_2(self):
        return self.driver.find_element(*AutothonControls.carousel_2)
    def get_carousel_3(self):
        return self.driver.find_element(*AutothonControls.carousel_3)
 
   
    def get_indian_express_allow_button(self):
        return self.driver.find_element(*AutothonControls.indian_express_allow_button)
    def get_indian_express_politics(self):
        return self.driver.find_element(*AutothonControls.indian_express_politics)    
    def get_indian_express_corousel(self):
        return self.driver.find_element(*AutothonControls.indian_express_corousel)
    def get_indian_express_headline(self):
        return self.driver.find_element(*AutothonControls.indian_express_headline)
    def get_indian_express_posted_date(self):
        return self.driver.find_element(*AutothonControls.indian_express_posted_date)