import logging

# Create a logger
logger = logging.getLogger(__name__)

# Configure the logger
logger.setLevel(logging.DEBUG)

# Create a handler to write the logs to a file
file_handler = logging.FileHandler('output.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))

# Add the handler to the logger
logger.addHandler(file_handler)

# Log a message

logger.info('Logging session started for new instance...')
logger.warning('This is a warning message [sample]')
logger.error('This is an error message [sample]')
