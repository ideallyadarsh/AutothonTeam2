import os
import time
import pandas
import numpy as np
import urllib.request
from PIL import Image, ImageChops
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from selenium.webdriver.common.by import By


class FileComparisonUtilities:
    """File Comparison Utilities contains the methods for file comparison related activities."""

    current_working_directory = os.path.dirname(os.getcwd())
    comparison_data = current_working_directory + "/Shell_FE_Behave_Tests/TestData/ExcelComparisons/"
    test_data = current_working_directory + "/Shell_FE_Behave_Tests/TestData/"
    test_img_data = current_working_directory + "\\Shell_FE_Behave_Tests\\TestData\\images\\"
    test_screenshot_data = current_working_directory + "\\Shell_FE_Behave_Tests\\TestData\\screenshots\\"
    log = LoggingUtilities().logger()

    @staticmethod
    def download_image(image='', svg = False,):
        """
        The method is used to download the image from the image xpath provided
        :param image: image xpath
        :param svg: True or False
        :return:
        """
        img_ele = SeleniumBase.driver.find_element(*image)
        img_src= img_ele.get_attribute("src")
        FileComparisonUtilities.log.info("Image source {0}".format(img_src))
        if svg == True:
            remote_img = "{}{}".format(FileComparisonUtilities.test_img_data, "remote.svg")
        else:
            remote_img = "{}{}".format(FileComparisonUtilities.test_img_data, "remote_file.png")
        urllib.request.urlretrieve(img_src, remote_img)
        FileComparisonUtilities.log.info("Image {0} downloaded successfully .".format(image))

    @staticmethod
    def compare_image(localimage='', remoteimage = '',svg = False, comp_type= 'image'):
        """
        This method will compare the screenshots or images and return the boolean result
        :param localimage: provide the base image name
        :param remoteimage: in case of image comparison provide image xpath
        :param svg: True or False
        :param comp_type: image or screenshot
        :return: True or False
        """
        FileComparisonUtilities.log.info("Images path {}".format(remoteimage))
        if comp_type == 'image':
            img_data = FileComparisonUtilities.test_img_data
            FileComparisonUtilities.download_image(remoteimage, svg = svg)
            loc_img = "{}{}".format(FileComparisonUtilities.test_img_data, localimage)
        elif comp_type == 'screenshot':
            img_data = FileComparisonUtilities.test_screenshot_data

        if svg == True:
            remote_img = "{}{}".format(img_data, "remote.svg")

            im3 = svg2rlg(r"{}".format(remote_img))
            im4 = svg2rlg(r"{}".format(loc_img))
            renderPM.drawToFile(im3, img_data+"remote_file.png", fmt="PNG")
            renderPM.drawToFile(im4, img_data + "local_file.png", fmt="PNG")

            im1 =  Image.open(r"{}".format(img_data+"remote_file.png"))
            im2 =  Image.open(r"{}".format(img_data + "local_file.png"))
        else:
            im1 =  Image.open(r"{}".format(img_data+"remote_file.png"))
            im2 =  Image.open(r"{}".format(img_data + localimage))

        diff = ImageChops.difference(im2, im1)
        tot_diff = np.mean(np.array(diff))
        os.remove(img_data + '/' + "remote_file.png")
        FileComparisonUtilities.log.info("Images differenece is {0}" .format(tot_diff))
        if tot_diff < 1 :
            FileComparisonUtilities.log.info("Images are same")
            return True
        else:
            FileComparisonUtilities.log.info("Images are NOT same")
            return False

    @staticmethod
    def compare_screenshot(local_image = None):
        """
        This method will download the screenshot of the current page and call the compare method to compare the local
        image with the downloaded image
        :param local_image: provide the base image name
        :return: result True or False
        """
        screenshot_img = "{}{}".format(FileComparisonUtilities.test_screenshot_data, "remote_file.png")
        SeleniumBase.driver.save_screenshot(screenshot_img)
        result = FileComparisonUtilities.compare_image(localimage= local_image, remoteimage='screenshot_img',comp_type='screenshot')
        return result

    @staticmethod
    def compare_excel(expected_file_name, actual_file_name):
        """The compare_excel method compares the given two excel files and returns a Boolean values based on the results of comparison.
        The method returns True if the files are equal and returns False if the files are not equal.
        Also, if the files are not equal a new excel file would be created containing the difference at the cell level.
        """
        expected_file = pandas.read_excel(FileComparisonUtilities.comparison_data + expected_file_name)
        actual_file = pandas.read_excel(FileComparisonUtilities.comparison_data + actual_file_name)

        if expected_file.equals(actual_file) is True:
            FileComparisonUtilities.log.info(
                f"The files {expected_file_name} and {actual_file_name} has been compared and found to be equal.")
            return True
        else:
            comparison_values = expected_file.values == actual_file.values
            rows, cols = np.where(comparison_values == False)
            for item in zip(rows, cols):
                expected_file.iloc[item[0], item[1]] = '{} --> {}'.format(expected_file.iloc[item[0], item[1]],
                                                                          actual_file.iloc[item[0], item[1]])
            timestamp = str(time.strftime("%d_%m_%H_%S")).replace("_", "")
            difference_excel = f"{FileComparisonUtilities.comparison_data}ExcelDifference{timestamp}.xlsx"
            expected_file.to_excel(difference_excel, index=False, header=True)
            FileComparisonUtilities.log.error(
                f"The compared files {expected_file_name} and {actual_file_name} are not equal and the differences "
                f"are captured in the file {difference_excel}.")
            return False

