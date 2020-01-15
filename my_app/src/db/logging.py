import logging
import logging.config

logging.config.fileConfig('my_app/src/config/logging.conf')
logger = logging.getLogger('simpleExample')