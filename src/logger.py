# Import the logging module, which provides a flexible framework for emitting log messages from Python programs.
import logging

# Import the os module, which provides a portable way of using operating system-dependent functionality.
import os

# Import the datetime class from the datetime module, which provides functions to work with dates and times.
from datetime import datetime

# Define a constant variable LOG_FILE, which contains the current date and time formatted as "month_day_year_hour_minute_second.log".
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Concatenate the current working directory and the "logs" directory with the LOG_FILE to create a logs_path.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the logs directory if it does not exist using os.makedirs(), and ensure that it is created even if it already exists (exist_ok=True).
os.makedirs(logs_path, exist_ok=True)

# Concatenate the logs_path and LOG_FILE to create the full path of the log file (LOG_FILE_PATH).
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system using basicConfig() method:
# - Set the filename parameter to specify the path of the log file.
# - Set the format parameter to define the format of log messages, including timestamp, line number, logger name, log level, and message.
# - Set the level parameter to specify the minimum logging level to be captured (INFO in this case).
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


