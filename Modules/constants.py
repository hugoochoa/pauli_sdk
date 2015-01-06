# -*- coding: utf-8 -*-

#  ██████╗ ██████╗ ███╗   ██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗███████╗
# ██╔════╝██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝██╔════╝
# ██║     ██║   ██║██╔██╗ ██║███████╗   ██║   ███████║██╔██╗ ██║   ██║   ███████╗
# ██║     ██║   ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║   ╚════██║
# ╚██████╗╚██████╔╝██║ ╚████║███████║   ██║   ██║  ██║██║ ╚████║   ██║   ███████║
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
                                                                               
# DESCRIPTION:
# Contains the global constants that are used (or could be used) in a Pauli's project.





# ======================================================== MODULE CODE

# Constants related to responses:
RESPONSE_TYPES = {
	'SUCCESS' : 1,
	'ERROR' : 0
}# End of RESPONSE_TYPES

# Https codes:
HTTP_CODES = {
	'SUCCESS' : 200,
	'BAD_REQUEST' : 400,
	'UNAUTHORIZED' : 401,
	'INTERNAL' : 500
}# End of HTTP_CODES

# Error messages:
ERROR_MESSAGES = {
	
	#Validating errors:
	'VALIDATING' : {
		'FUNCTION_EXISTANCE' : 'API function called does not exist ',
		'PARAMS_EXISTANCE' : 'API function called without params ',
		'PARAMS_INVALIDATED' : 'API function called with invalid params ',
		'INVALID_PRIVATE_FUNCTION_CALLING' : 'Invalid private API key'
	},# End of VALIDATING

	#Internal errors:
	'INTERNAL' : 'Internal Server Error '

}# End of ERROR_MESSAGES

# Success messages:
SUCCESS_MESSAGES = {
	
	#Validating errors:
	'VALIDATING' : {
		'REQUEST_VALIDATED' : 'Valid request'
	}# End of VALIDATING

}# End of ERROR_MESSAGES

# Logging standard messages:
REQUEST_BEGINNING_MESSAGE_1 = '\n ------------------------------------------------------------------------------------------------------ \n \n     '
REQUEST_BEGINNING_MESSAGE_2 = ' Pauli´s Project - Listen '
REQUEST_BEGINNING_MESSAGE_3 = ' request. \n'
VALIDATING_REQUEST_MESSAGE = 'Validating request'
INVALID_REQUEST_MESSAGE = 'Invalid request.'
EXECUTING_REQUEST_MESSAGE = 'Executing request. API function: '
FUNCTION_EXECUTION_BEGINNING_MESSAGE = 'Function execution beginning'
FUNCTION_EXECUTION_ENDING_MESSAGE = 'Function execution ending'
REQUEST_ENDING_MESSAGE = 'Sending response \n \n     <- API - Request ended. \O/ \n \n \n \n \n \n \n'
STARTING_SERVER = ' * Starting API Server on private port: '
STABILISH_DB_CONNECTINON = ' * Stablishing DB connection to '
STARTING_SERVER_ERROR = 'Error starting server: '
LOGGING_ERROR = 'Logging error: '

# Params validation properties:
LIST_ITEM_SPECIFICATION = 'list_item_specification'
DICT_ITEM_SPECIFICATION = 'dict_item_specification'
REQUIRED_PARAMS = 'required_params'
VALUE_TYPE = 'value_type'
PARAM_TYPE = 'param_type'
OBLIBATORY_PARAM = 'Obligatory'
OPTIONAL_PARAM = 'Optional'
INSTANCE = 'instance'
PUBLIC_FUNCTION = 'public_function'
PRIVATE_FUNCTION = 'private_function'
PRIVATE_API_KEY = 'private_API_key'





