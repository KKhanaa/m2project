# Import the sys module, which provides access to system-specific parameters and functions.
import sys

# Import the logging object from a custom source located in the src/logger.py file.
from src.logger import logging

# Define a function named error_message_detail that takes two arguments: error and error_detail.
def error_message_detail(error, error_detail: sys):
    # Extract information about the error using error_detail.exc_info() and assign it to the variables (_, _, exc_tb).
    _, _, exc_tb = error_detail.exc_info()
    # Retrieve the filename where the error occurred from the traceback object and assign it to the variable file_name.
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Construct a detailed error message string containing the filename, line number, and error message.
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    # Return the error message.
    return error_message

# Define a custom exception class named CustomException, which inherits from the built-in Exception class.
class CustomException(Exception):
    # Define the __init__ method, which initializes a new instance of the CustomException class.
    def __init__(self, error_message, error_detail: sys):
        # Call the __init__ method of the superclass (Exception) with the provided error_message.
        super().__init__(error_message)
        # Generate a detailed error message using the error_message_detail function and assign it to the error_message attribute.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    # Define the __str__ method, which returns a string representation of the CustomException object.
    def __str__(self):
        # Return the detailed error message.
        return self.error_message
