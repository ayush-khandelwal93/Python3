# SEE basic4 to see how default root logger can be used
# Here we are using our own custom logger

import logging

logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO) 
#Default logger is level of warning, so logger.info is not in output

handler = logging.FileHandler('basic3.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(mess\
age)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('Hello baby')
logger.warning('Warning')
