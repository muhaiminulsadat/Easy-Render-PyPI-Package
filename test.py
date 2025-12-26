from EasyRender.logger import logger
from EasyRender.custom_exception import InvalidURLException

# logger.info('This is a test log message from test.py')
try:
    raise InvalidURLException()
except Exception as e :
    logger.error(e)