import  pytest
import logging
@pytest.mark.usefixtures("browser")
class Baseclass:
    def log(self):
        logger = logging.getLogger(__name__)
        filehandler= logging.FileHandler("log1.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger