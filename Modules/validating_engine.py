# -*- coding: utf-8 -*-

# ██╗   ██╗ █████╗ ██╗     ██╗██████╗  █████╗ ████████╗██╗███╗   ██╗ ██████╗     ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
# ██║   ██║██╔══██╗██║     ██║██╔══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝     ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
# ██║   ██║███████║██║     ██║██║  ██║███████║   ██║   ██║██╔██╗ ██║██║  ███╗    █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
# ╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║██╔══██║   ██║   ██║██║╚██╗██║██║   ██║    ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
#  ╚████╔╝ ██║  ██║███████╗██║██████╔╝██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝    ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
#   ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                                               
# DESCRIPTION:
# Validate Pauli's project API calls and execute its respective API function





# ======================================================== DEPENDENCIES

# Native:
import logging
import sys

# Development:
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Validating_Exception
from pauli_sdk.Classes.response import Already_Handled_Exception





# ======================================================== MODULE CODE

logger = logging.getLogger('root')




# Some constants:
required_params = _Pauli_Constants.REQUIRED_PARAMS
value_type = _Pauli_Constants.VALUE_TYPE
param_type = _Pauli_Constants.PARAM_TYPE
obligatory = _Pauli_Constants.OBLIBATORY_PARAM
optional = _Pauli_Constants.OPTIONAL_PARAM






    #            ██╗      ██████╗ ██╗   ██╗██████╗ ██╗     ██╗ ██████╗     ██████╗ ██████╗ ██████╗ ███████╗
    #            ╚██╗     ██╔══██╗██║   ██║██╔══██╗██║     ██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
    # █████╗█████╗╚██╗    ██████╔╝██║   ██║██████╔╝██║     ██║██║         ██║     ██║   ██║██║  ██║█████╗  
    # ╚════╝╚════╝██╔╝    ██╔═══╝ ██║   ██║██╔══██╗██║     ██║██║         ██║     ██║   ██║██║  ██║██╔══╝  
    #            ██╔╝     ██║     ╚██████╔╝██████╔╝███████╗██║╚██████╗    ╚██████╗╚██████╔╝██████╔╝███████╗
    #            ╚═╝      ╚═╝      ╚═════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝





# Validate requests:
def validate(request_data,_pauli_project_config_file):

	try:

		logger.info(_Pauli_Constants.VALIDATING_REQUEST_MESSAGE)
		function_called = request_data['function']
		function_params = request_data['params']
		# Validate API function existance:
		if not function_called in _pauli_project_config_file.functions:
			validating_error_response = Error(_Pauli_Constants.HTTP_CODES['BAD_REQUEST'],_Pauli_Constants.ERROR_MESSAGES['VALIDATING']['FUNCTION_EXISTANCE'])
			raise Validating_Exception(validating_error_response)
		# Validate API function params existance:
		if not function_params:
			validating_error_response = Error(_Pauli_Constants.HTTP_CODES['BAD_REQUEST'],_Pauli_Constants.ERROR_MESSAGES['VALIDATING']['PARAMS_EXISTANCE'])
			raise Validating_Exception(validating_error_response)
		# Validate API function params: 
		if not validate_params(function_called,function_params,_pauli_project_config_file):
			validating_error_response = Error(_Pauli_Constants.HTTP_CODES['BAD_REQUEST'],_Pauli_Constants.ERROR_MESSAGES['VALIDATING']['PARAMS_INVALIDATED'])
			raise Validating_Exception(validating_error_response)
		# Validate API private/public calling:
		if not validate_private_or_public_API_call(function_called,function_params,_pauli_project_config_file):
			validating_error_response = Error(_Pauli_Constants.HTTP_CODES['BAD_REQUEST'],_Pauli_Constants.ERROR_MESSAGES['VALIDATING']['PARAMS_INVALIDATED'])
			raise Validating_Exception(validating_error_response)
		# Valid request: 
		return True

	# Handle validating exception (i.e. validating error)
	except Validating_Exception as validating_exception:

		# Built error from exception
		validating_error = validating_exception.value
		# Log error:
		logger.critical('Code: ' + str(validating_error.http_code) + '    Message: ' + str(validating_error.content))
		# Exception was already handled (i.e. error was built and logged in this except) so it is transformed into an already handled exception:
		already_handled_exception = Already_Handled_Exception(validating_error)
		# Raise exception to outer except(s)
		raise already_handled_exception

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






    #            ██╗      ██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ████████╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗
    #            ╚██╗     ██╔══██╗██╔══██╗██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
    # █████╗█████╗╚██╗    ██████╔╝██████╔╝██║██║   ██║███████║   ██║   █████╗      ██║     ██║   ██║██║  ██║█████╗  
    # ╚════╝╚════╝██╔╝    ██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝      ██║     ██║   ██║██║  ██║██╔══╝  
    #            ██╔╝     ██║     ██║  ██║██║ ╚████╔╝ ██║  ██║   ██║   ███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗
    #            ╚═╝      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                   




# Validate request params:
def validate_params(function_called,given_params,_pauli_project_config_file):

	try: 

		# Validation:
		function_required_params = _pauli_project_config_file.functions[function_called][required_params]
		# Validate the given params dictionary (json):
		params_validation = validate_dict(given_params,function_required_params)
		# Rerturn validation
		return params_validation# A boolean

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





# Validate the structure of a dictionary (i.e. key-value content-type recursively)
def validate_dict(given_dict,dict_item_specification):# dict_item_specification is an element of _pauli_project_config_file functions

	try:

		for required_dict_key in dict_item_specification:
			# Obligatory param:
			if dict_item_specification[required_dict_key][param_type] == obligatory:
				if not required_dict_key in given_dict:
					logger.info(dict_item_specification[required_dict_key][param_type] + ' param ' + str(required_dict_key) + ' must exist')
					return False# If an olbligatory param does not exist params are not validated
			# Optional param:
			elif dict_item_specification[required_dict_key][param_type] == optional:
				if not required_dict_key in given_dict:
					continue# If an optional param does not exist just go to the next param
			# Param value type validation:
			required_dict_value_type = dict_item_specification[required_dict_key][value_type]
			given_dict_value = given_dict[required_dict_key]
			given_dict_value_type = type(given_dict_value)
			if not given_dict_value_type == required_dict_value_type:
				logger.info(dict_item_specification[required_dict_key][param_type] + ' param ' + str(required_dict_key) + ' is not valid in type')
				return False
			if required_dict_value_type == list:
				inner_list = given_dict_value
				inner_list_item_specification = dict_item_specification[required_dict_key]['list_item_specification']
				inner_list_validation = validate_list(inner_list,inner_list_item_specification)
				if inner_list_validation == False:
					return False
			elif required_dict_value_type == dict:
				inner_dict = given_dict_value
				inner_dict_item_specification = dict_item_specification[required_dict_key]['dict_item_specification']
				inner_dict_validation = validate_dict(inner_dict,inner_dict_item_specification)
				if inner_dict_validation == False:
					return False
		return True

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





# Validate de structure of a list (i.e. item-value content-type recursively)
def validate_list(given_list,list_item_specification):# list_item_specification is an element of _pauli_project_config_file functions

	try: 

		required_list_item_type = list_item_specification[value_type]
		for list_item in given_list:
			list_item_type = type(list_item)
			if not list_item_type == required_list_item_type:
				logger.info('List item is not valid in type')
				return False
			if required_list_item_type == list:
				inner_list = list_item
				inner_list_item_specification = list_item_specification['list_item_specification']
				inner_list_validation = validate_list(inner_list,inner_list_item_specification)
				if inner_list_validation == False:
					return False
			elif required_list_item_type == dict:
				inner_dict = list_item
				inner_dict_item_specification = list_item_specification['dict_item_specification']
				inner_dict_validation = validate_dict(inner_dict,inner_dict_item_specification)
				if inner_dict_validation == False:
					return False
		return True

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





# Validate request private API key:
def validate_private_or_public_API_call(function_called,given_params,_pauli_project_config_file):

	try: 

		function_information = _pauli_project_config_file.functions[function_called];
		# Public functions validation:
		if is_a_public_function(function_information):
			return True
		if is_a_private_function(function_information):
			# Validation:
			private_API_Key_given = given_params[_Pauli_Constants.PRIVATE_API_KEY]
			if private_API_Key_given == _pauli_project_config_file.general[_Pauli_Constants.PRIVATE_API_KEY]:
				return True
			else:
				return False

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






# Check if a function is public:
def is_a_public_function(function_information):# Function information is the one given in _pauli_project_config_file.functions

	try:

		is_a_public_function = False
		if _Pauli_Constants.PUBLIC_FUNCTION in function_information and function_information[_Pauli_Constants.PUBLIC_FUNCTION] == True:
			is_a_public_function = True
		return is_a_public_function

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






# Check if a function is private:
def is_a_private_function(function_information):# Function information is the one given in _pauli_project_config_file.functions

	try:

		is_a_private_function = False
		if _Pauli_Constants.PRIVATE_FUNCTION in function_information and function_information[_Pauli_Constants.PRIVATE_FUNCTION] == True:	
			is_a_private_function = True
		return is_a_private_function

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















