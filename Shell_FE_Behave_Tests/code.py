from appium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import os
import requests

# # Desired capabilities for the Appium driver
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': 'Android Emulator',
#     'appPackage': 'com.instagram.android',
#     'appActivity': '.activity.MainTabActivity',
#     'automationName': 'UiAutomator2'
# }

# # Check if the Appium server is running
# def is_appium_server_running(url='http://localhost:4723/wd/hub'):
#     try:
#         response = requests.get(url + '/status')
#         if response.status_code == 200:
#             return True
#     except requests.ConnectionError:
#         pass
#     return False

# if not is_appium_server_running():
#     print("Appium server is not running. Please start the Appium server and try again.")
#     exit(1)

# # Initialize the Appium driver
# try:
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     print("Driver initialized successfully.")
# except WebDriverException as e:
#     print(f"Failed to initialize driver: {e}")
#     exit(1)

# # Give some time for the app to load
# time.sleep(5)

# # Log into Instagram (placeholder for actual login logic)
# print("Logging into Instagram...")

# # Path to the local image and the destination path on the device
# local_image_path = 'path/to/local/image.jpg'
# device_image_path = '/sdcard/Download/image.jpg'

# # Check if the local image file exists
# if not os.path.exists(local_image_path):
#     print(f"Local image file does not exist: {local_image_path}")
#     driver.quit()
#     exit(1)

# # Read the image file in binary mode
# try:
#     with open(local_image_path, 'rb') as image_file:
#         image_data = image_file.read()
    
#     # Push the image file to the device
#     driver.push_file(device_image_path, image_data)
#     print(f"Image transferred to {device_image_path}")
# except Exception as e:
#     print(f"Failed to transfer image: {e}")

# # Quit the driver
# driver.quit()
# print("Driver quit successfully.")