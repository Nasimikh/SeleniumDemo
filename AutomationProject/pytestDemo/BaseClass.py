# Logger gets stored in a base class for re-usability purposes

import inspect
import logging


class BaseClass:

    @staticmethod
    def getlogger():
        logname = inspect.stack()[1][3]
        log = logging.getLogger(logname)
        filehandler = logging.FileHandler("fix-logs.log")
        log.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")
        filehandler.setFormatter(formatter)

        log.setLevel(logging.INFO)
        return log
