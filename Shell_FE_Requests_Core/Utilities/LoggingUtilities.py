import inspect
import logging
import os
import time


class LoggingUtilities:
    logFolder = os.path.dirname(os.getcwd()) + '/Shell_FE_Behave_Tests/TestResults/Logs/'

    def logger(self, filename="logfile"+str(time.strftime("%d_%m_%H_%S")).replace("_", "")+".log"):
        """Creates logger instance with predefined format for logs.

        :Args:
            - filename - Filename for the log file. Has a default value "logfile.log".

        Returns:
            Logger instance
        """
        logger = logging.getLogger(inspect.stack()[1][3])
        logger.setLevel("DEBUG")
        filehandler = logging.FileHandler(LoggingUtilities.logFolder + filename, "a")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(funcName)s :%(message)s")
        # formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        return logger
