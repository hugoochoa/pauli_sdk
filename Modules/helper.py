# -*- coding: utf-8 -*-

# ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
# ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
# ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
# ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
# ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
# ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                
# DESCRIPTION:
# Contains all the recycle functions that are used in a Pauli's project





# ======================================================== DEPENDENCIES

# Native:
import logging
import sys

# Development:
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Classes.response import Success
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Already_Handled_Exception

# External:
from pymongo import MongoClient 



# ======================================================== CODE MODULE

logger = logging.getLogger('root')




DB_NAME = None
DB_PORT = None
DB_HOST = None

# Set db connection:
def set_db_connection():

	try:

		# Stablish DB connection:
		mongo = MongoClient(DB_HOST,DB_PORT)
		db = mongo[DB_NAME]
		return db# Mongo db object

	# Handle other exception (i.e. internal server error)
	except:

		# Get exception:
		other_exception = str(sys.exc_info()[1])
		# Build error from exception:
        other_error = Error(_Pauli_Constants.HTTP_CODES['INTERNAL'],_Pauli_Constants.ERROR_MESSAGES['INTERNAL'])
		# Log exception/error:
        logger.critical(other_error.content + other_exception)
        # Exception was already handled (i.e. error was built and logged int this except) so it is transformed into an already handled exception:
        already_handled_exception = Already_Handled_Exception(other_error)
        # Raise exception to outer except(s):
        raise already_handled_exception
























