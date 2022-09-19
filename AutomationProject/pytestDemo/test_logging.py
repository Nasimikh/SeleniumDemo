import logging


def test_logdemo():
    log = logging.getLogger(__name__)
    filehandler = logging.FileHandler("fix-logs.log")
    log.addHandler(filehandler)
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")
    filehandler.setFormatter(formatter)

    log.setLevel(logging.ERROR)
    log.debug("Debug statement is executed:")
    log.info("Info statement is executed:")
    log.error("Error handler:")
    log.warning("After purchasing this item your balance will be negative:")
    log.critical("Critical issue found:")
