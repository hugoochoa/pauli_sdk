# -*- coding: utf-8 -*-

# ███████╗ ██████╗ ███╗   ███╗███████╗    ███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗
# ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝
# ███████╗██║   ██║██╔████╔██║█████╗      ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  
# ╚════██║██║   ██║██║╚██╔╝██║██╔══╝      ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  
# ███████║╚██████╔╝██║ ╚═╝ ██║███████╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗
# ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                                             
# DESCRIPTION:
# Contains some logic of our project:




# ======================================================== DEPENDENCIES

# Native:
import logging
import sys

# Development:
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Modules import helper as _Pauli_Helper
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Already_Handled_Exception
from Modules import constants as _Constants







# ======================================================== MODULE CODE

logger = logging.getLogger('root')

# Our public function explanation must be here:
def our_public_function_instance(params):

	try:

		logger.info(_Pauli_Constants.FUNCTION_EXECUTION_BEGINNING_MESSAGE)
			
			# ... our public function logic must be here ...
		
		logger.info(_Pauli_Constants.FUNCTION_EXECUTION_ENDING_MESSAGE)

		return 'our_PUBLIC_function executed succesfully'

	# Exception was already handled (i.e. error was built and logged in a deeper except) so it just raised to outer excepts(s):
	except Already_Handled_Exception as already_handled_exception:

		# Raise exception to outer except(s)
		raise already_handled_exception

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











# Our private function explanation must be here:
def our_private_function_instance(params):

	try:

		logger.info(_Pauli_Constants.FUNCTION_EXECUTION_BEGINNING_MESSAGE)
			
			# ... our private function logic must be here ...
		
		logger.info(_Pauli_Constants.FUNCTION_EXECUTION_ENDING_MESSAGE)

		return 'our_PRIVATE_function executed succesfully'

	# Exception was already handled (i.e. error was built and logged in a deeper except) so it just raised to outer excepts(s):
	except Already_Handled_Exception as already_handled_exception:

		# Raise exception to outer except(s)
		raise already_handled_exception

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










