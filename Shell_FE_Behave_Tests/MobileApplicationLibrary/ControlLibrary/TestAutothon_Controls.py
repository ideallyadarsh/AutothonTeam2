from appium.webdriver.common.mobileby import MobileBy


class TestAutothon_Controls:

    def __init__(self, driver):
        self.driver = driver

    get_products = (MobileBy.XPATH, '//android.widget.TextView[@text="Get Products"]')
    name = (MobileBy.XPATH, '((//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View)[<n>]/android.widget.TextView)[1]')
    description = (MobileBy.XPATH, '((//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View)[<n>]/android.widget.TextView)[2]')
    price = (MobileBy.XPATH, '((//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View)[<n>]/android.widget.TextView)[3]')

    def get_get_products(self):
        return self.driver.find_element(*TestAutothon_Controls.get_products)
    def get_name(self, n):
        return self.driver.find_element(*TestAutothon_Controls.name.replace('<n>', n))
    def get_description(self, n):
        return self.driver.find_element(*TestAutothon_Controls.description.replace('<n>', n))
    def get_price(self, n):
        return self.driver.find_element(*TestAutothon_Controls.price.replace('<n>', n))
    def get_dynamic_element(self, element, n):
        xpath = self.__getattribute__(element)[1].replace('<n>', n)
        return self.driver.find_element(MobileBy.XPATH, xpath)
    