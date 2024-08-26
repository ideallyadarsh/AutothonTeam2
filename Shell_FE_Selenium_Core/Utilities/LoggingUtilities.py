import inspect
import logging
import os
import time
import allure


class AllureLoggingHandler(logging.Handler):
    def allureLog(self, level_name, message):
        with allure.step(f"Log ({level_name}) {message}"):
            if level_name.lower() == "info":
                assert True
            else:
                assert False

    def emit(self, record):
        self.allureLog(record.levelname, record.getMessage())


class LoggingUtilities:
    logFolder = os.path.dirname(os.getcwd()) + '/Shell_FE_Behave_Tests/TestResults/Logs/'

    def logger(self, filename="logfile" + str(time.strftime("%d_%m_%H_%S")).replace("_", "") + ".log"):
        """Creates logger instance with predefined format for logs.

        :Args:
            - filename - Filename for the log file. Has a default value "logfile.log".

        Returns:
            Logger instance
        """
        logger = logging.getLogger(inspect.stack()[1][3])
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.setLevel("DEBUG")
        logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s",
                            datefmt='%d/%m/%Y- %I:%M:%S %p')
        filehandler = logging.FileHandler(LoggingUtilities.logFolder + filename, "a")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(funcName)s :%(message)s")
        # formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
        allure_handler = AllureLoggingHandler()
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.addHandler(allure_handler)
        return logger
