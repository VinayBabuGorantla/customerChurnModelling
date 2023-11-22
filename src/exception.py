import sys
from src.logger import logging

def error_message_detail(error, exception_info: sys):
    _, _, exc_tb = exception_info
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, exception_info: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, exception_info=exception_info)
    
    def __str__(self):
        return self.error_message