from Shell_FE_Appium_Core.AppiumBase import AppiumBase
from Shell_FE_Appium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Behave_Tests.MobileApplicationLibrary.ControlLibrary.TestAutothon_Controls import TestAutothon_Controls
from Shell_FE_Appium_Core.Utilities.WaitUtilities import WaitUtilities
from Shell_FE_Appium_Core.Utilities.AssertUtilities import AssertUtilities
from Shell_FE_Appium_Core.Utilities.AndroidUtilities import AndroidUtilities
from Shell_FE_Requests_Core.RequestsBase import RequestsBase
import time
import base64


class TestAutothon_Functions:
    log = LoggingUtilities()
    log_file = log.logger()

    def __init__(self):
        self.TestAutothon_Controls = TestAutothon_Controls(AppiumBase.driver)
        self.product_details = []
        self.base_url = "http://ec2-54-254-162-245.ap-southeast-1.compute.amazonaws.com:9000/items/"
        self.team_name = "Shell India - 1"
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

    def post_product_details(self, product_name, product_description, product_price, team_name):
        headers = {     
            'Content-Type': 'application/json'  
        }
        data = {
        "name": product_name,
        "description": product_description,
        "price": int(product_price.split(" ")[0].replace("-", "")),
        "item_type": team_name,
        }
        AndroidUtilities.log.info(f"Product Details: \Name: {product_name} \nDescription: {product_description} \nPrice: {product_price} \nTeam Name: {team_name}")
        RequestsBase.post_request(url = self.base_url, headers= headers, body_json= data)

    def validate_product_details(self, product_name, product_description, product_price, team_name, id):
        RequestsBase.get_request(url = self.base_url + str(id))
        if RequestsBase.response_status_code(RequestsBase.response) != 200:
            
            AndroidUtilities.log.error(f"Retrieval of Product with ID: {id} failed \nResponse received: {RequestsBase.response_body_as_string(RequestsBase.response)}")
        AndroidUtilities.log.info(f"Successful Retrieval of Product with ID: {id} \nResponse received: {RequestsBase.response_body_as_string(RequestsBase.response)}")
        response = RequestsBase.response_body_as_dictionary(RequestsBase.response)

        if response.get("name") == product_name and response.get("description") == product_description and int(response.get("price")) == int(float(product_price)) and response.get("item_type") == team_name:
            AndroidUtilities.log.info(f"Successful validation for Product with ID: {id}")
        else:
            AndroidUtilities.log.error(f"Validation failed for Product with ID: {id} \nResponse received: {RequestsBase.response_body_as_string(RequestsBase.response)}")

    def post_and_validate_product_details(self):
        for i in range(len(self.product_details)):
            self.log_file.info('-'*60)
            self.post_product_details(self.product_details[i][0],self.product_details[i][1],self.product_details[i][2], self.team_name)
            # response = API.post(self.product_details[i][0],self.product_details[i][1],self.product_details[i][2])
            if RequestsBase.response_status_code(RequestsBase.response) != 200:
                AndroidUtilities.log.error(f"Product was not posted \nResponse received: {RequestsBase.response_body_as_string(RequestsBase.response)}") 

            id = RequestsBase.response_body_as_dictionary(RequestsBase.response).get("id")
            AndroidUtilities.log.info(f"Product posted successfully with id {id}...")

            self.validate_product_details(self.product_details[i][0],self.product_details[i][1],self.product_details[i][2], self.team_name ,id)


    


