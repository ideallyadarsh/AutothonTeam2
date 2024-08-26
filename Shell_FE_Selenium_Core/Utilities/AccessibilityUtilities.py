import os
import time
from axe_selenium_python import Axe
from Shell_FE_Selenium_Core.SeleniumBase import SeleniumBase
from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities


class AccessibilityUtilities:
    """AccessibilityUtilities contains reusable methods to perform Accessibility testing using Axe."""

    logobj = LoggingUtilities()
    log = logobj.logger()

    reportFolder = os.path.dirname(os.getcwd()) + '/Shell_FE_Behave_Tests/TestResults/Logs/'

    @staticmethod
    def analyze_page():
        """Validates the current webpage for accessibility checks and creates a JSON report of accessibility results under the Logs folder.

        :Returns:
            - Number of accesibility violations present in the web page.
        """
        report_name = "WebAccessibilityReport" + str(time.strftime("%d_%m_%H_%S")).replace("_", "") + ".json"
        axe = Axe(SeleniumBase.driver)
        axe.inject()
        results = axe.run()
        axe.write_results(results, AccessibilityUtilities.reportFolder + report_name)
        AccessibilityUtilities.log.info("Accessibility report has been generated and saved as {0} in the Logs folder.".format(report_name))
        no_of_violations = len(results["violations"])
        if no_of_violations > 0:
            AccessibilityUtilities.log.error("Accessibility test for the web page failed due to violations present. Check the report {0}.".format(report_name))

        return no_of_violations

