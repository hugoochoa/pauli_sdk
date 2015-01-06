# -*- coding: utf-8 -*-

# ██╗      ██████╗  ██████╗ 
# ██║     ██╔═══██╗██╔════╝ 
# ██║     ██║   ██║██║  ███╗
# ██║     ██║   ██║██║   ██║
# ███████╗╚██████╔╝╚██████╔╝
# ╚══════╝ ╚═════╝  ╚═════╝ 
                          
# DESCRIPTION:
# Contains logging supporting for information, warning and debugging a Pauli's project





# ======================================================== DEPENDENCIES

# Development:
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Already_Handled_Exception

# Native:
import sys
import logging
from logging.handlers import TimedRotatingFileHandler





# ======================================================== MODULE CODE

# Set logger:
def setup_custom_logger(name,_pauli_project_config_file):

	try:

		formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(module)s - %(funcName)s:%(lineno)d - %(message)s','%Y-%m-%d %H:%M:%S')
		handler = TimedRotatingFileHandler(_pauli_project_config_file.general['logging_root'] + '/' + _pauli_project_config_file.general['logging_file_default_name'], when='midnight')
		handler.setFormatter(formatter)
		logger = logging.getLogger(name)
		logger.setLevel(logging.DEBUG)		
		logger.addHandler(handler)
		return logger

	# Handle other exception (i.e. internal server error)
	except:

		# Get exception:
		other_exception = str(sys.exc_info()[1])
        # Log exception/error:
        print _Pauli_Constants.LOGGING_ERROR + other_exception
        # Exception was already handled (i.e. error was built and logged int this except) so it is transformed into an already handled exception:
        already_handled_exception = Already_Handled_Exception('Logging could not be started')
        # Raise exception to outer except(s):
        raise already_handled_exception








