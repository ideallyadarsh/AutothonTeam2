from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.TestAutothon_Controls import TestAutothon_Controls
from Shell_FE_Behave_Tests.ApiLibrary.API import API
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
import time
import base64


class TestAutothon_Functions:
    log = LoggingUtilities()
    log_file = log.logger()

    def __init__(self):
        self.TestAutothon_Controls = TestAutothon_Controls(AppiumBase.driver)
        self.product_details = []
        # with open("..\..\Web_Autothon\Shell_FE_Behave_Tests\TestData\Images\tweet.png", 'rb') as image_file:
        #     image_data = image_file.read()
        # AppiumBase.driver.push_file("/storage/emulated/0/DCIM/image.png", image_data)

    def click_get_products(self):
        AndroidUtilities.click_element(self.TestAutothon_Controls.get_get_products())

    def get_add_products(self,name,description,price):
        self.product_details.append([name,description,price])

    def get_product_details(self):
        for i in range(1, 4):
            name = AndroidUtilities.get_text(self.TestAutothon_Controls.get_dynamic_element("name",str(i)))
            description = AndroidUtilities.get_text(self.TestAutothon_Controls.get_dynamic_element("description",str(i)))
            price = AndroidUtilities.get_text(self.TestAutothon_Controls.get_dynamic_element("price",str(i))).replace("₹",'')
            self.log_file.info(f"Product Name: {name} Description: {description} Price: {price}")
            self.get_add_products(name,description,price)

        self.log_file.info(self.product_details)

    def post_and_validate_product_details(self):
        for i in range(len(self.product_details)):
            self.log_file.info('-'*60)
            response = API.post(self.product_details[i][0],self.product_details[i][1],self.product_details[i][2])
            if response:
                self.log_file.info(f"Product {i+1} posted successfully")
                validation = API.validate(self.product_details[i][0],self.product_details[i][1],self.product_details[i][2],response)
                if validation:
                    self.log_file.info(f"Product {i+1} validated successfully. Id :{validation}")
                else:
                    self.log_file.error(f"Product {i+1} not validated successfully. Id :{validation}")
                    raise AssertionError(f"Product {i+1} not validated successfully. Id :{validation}")
            else:
                self.log_file.error(f"Product with ID: {id} not posted successfully")

    


