# __init__.py

# from .UserDetails_Tracker import *
import pkg_resources
from .ActiveUserDetails import *

PACKAGE_NAME = 'Shell_FE_Selenium_Core'
try:
    PACKAGE_VERSION = pkg_resources.get_distribution(PACKAGE_NAME).version
except pkg_resources.DistributionNotFound:
    PACKAGE_VERSION = 'unknown'


# UserDetails.collect_details(PACKAGE_NAME, PACKAGE_VERSION)
# dbconnectiontrigger.details.collect_details(PACKAGE_NAME, PACKAGE_VERSION)
ActiveUserDetails.ActiveUsers.collect_user_details(PACKAGE_NAME, PACKAGE_VERSION)
