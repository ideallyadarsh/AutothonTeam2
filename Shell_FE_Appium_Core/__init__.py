import pkg_resources
from .ActiveUserDetails import *

PACKAGE_NAME = 'Shell_FE_Appium_Core'
try:
    PACKAGE_VERSION = pkg_resources.get_distribution(PACKAGE_NAME).version
except pkg_resources.DistributionNotFound:
    PACKAGE_VERSION = 'unknown'


ActiveUserDetails.ActiveUsers.collect_user_details(PACKAGE_NAME, PACKAGE_VERSION)
