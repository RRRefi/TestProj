import logging
import time
import os
from base.public import filePath

class Logger(object):
    def __init__(self, logger_name=None, level='info'):
        log_path = filePath('log')
        os.makedirs(log_path, exist_ok=True)
        
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.logFileName = time.strftime("%y_%m_%d_") + f'_{logger_name}.log'
        self.backupCount = 5

        level = level.upper()
        self.consoleOutputLevel = getattr(logging, level, logging.INFO)
        self.fileOutputLevel = getattr(logging, level, logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s'
        )
        
        file_handler = logging.FileHandler(
            os.path.join(log_path, self.logFileName), 
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(self.fileOutputLevel)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(self.consoleOutputLevel)
        
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

# 实例化全局logger
logger = Logger(logger_name='api_auto_test').get_logger()