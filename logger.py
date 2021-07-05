import logging


class Logger(object):
    def __init__(self, name):

        self.log = logging.getLogger(name)

        self.file_handler = logging.FileHandler('C:/temp/atest.log')
        self.file_handler.setFormatter(self.formatter)

        self.log.addHandler(self.file_handler)
        self.log.setLevel(logging.DEBUG)

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.file_handler.close()
        self.log.removeHandler(self.file_handler)

    @property
    def formatter(self):
        return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def info(self, msg):
        self.log.info(msg)

    def error(self, msg):
        self.log.error(msg)

    def warning(self, msg):
        self.log.warning(msg)


if __name__ == '__main__':
#
    log = Logger("Test")
    log.info("it is a test")
#
    log.error("and this is an error")
