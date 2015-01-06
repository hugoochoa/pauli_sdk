# -*- coding: utf-8 -*-

# ███╗   ███╗ █████╗ ██╗███╗   ██╗
# ████╗ ████║██╔══██╗██║████╗  ██║
# ██╔████╔██║███████║██║██╔██╗ ██║
# ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
# ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
                                                                                                                
# DESCRIPTION:
# Pauli project main file. It just starts API, listens request, redirect to application logic









# ======================================================== DEPENDENCIES

# Native:
import os, sys, json

# External:
from flask import Flask
from flask import request

# Load SDK:
pauli_storage_path = '/usr/local/lib'
pauli_storage_absolute_path = os.path.abspath(pauli_storage_path)
sys.path.append(pauli_storage_absolute_path)
from pauli_sdk.Classes.response import Success
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Already_Handled_Exception
from pauli_sdk.Modules import log as _Log
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Modules import helper as _Pauli_Helper
from pauli_sdk.Modules import validating_engine as _Validating_Engine
from pauli_sdk.Modules import request_handler as _Request_Handler

# Get configuration
from Configuration import config as _Config




# ======================================================== MODULE CODE

# Api constructor:
app = Flask(__name__)

# Pauli's project configuration:
Pauli_project_name = _Config.general['project_name'].upper()
Pauli_project_private_port = _Config.general['pauli_project_private_port']
Pauli_project_main_path = _Config.general['main_path']
Pauli_project_main_dynamic_path = Pauli_project_main_path + '/<dynamic_path>'









#   ___  ______ _____ 
#  / _ \ | ___ \_   _|
# / /_\ \| |_/ / | |  
# |  _  ||  __/  | |  
# | | | || |    _| |_ 
# \_| |_/\_|    \___/ 
                    
def api(request_data,rest_method):

	# Log beginning of request:
	REQUEST_BEGINNING_MESSAGE = _Pauli_Constants.REQUEST_BEGINNING_MESSAGE_1 + Pauli_project_name + _Pauli_Constants.REQUEST_BEGINNING_MESSAGE_2 + rest_method + _Pauli_Constants.REQUEST_BEGINNING_MESSAGE_3
	logger.info(REQUEST_BEGINNING_MESSAGE)

	try:

		# Validating:
		if _Validating_Engine.validate(request_data,_Config):
			# Executing:
			result = _Request_Handler.execute(request_data,_Config)
			# Build success result:
			success = Success(result)
			# Build response:
			response = success.get_response()

	# Exception was already handled (i.e. error was built and logged in a deeper except) so error is extracted an response is built
	except Already_Handled_Exception as already_handled_exception:

		# Get inner error:
		inner_error = already_handled_exception.value
		# Build response:
		response = inner_error.get_response()

	# Handle other exception, build error and response:
	except:

		# Get exception
		other_exception = str(sys.exc_info()[1])
		# Build error from exception
		other_error = Error(_Pauli_Constants.HTTP_CODES['INTERNAL'],_Pauli_Constants.ERROR_MESSAGES['INTERNAL'])
		# Log exception/error:
		logger.critical(other_error.content + other_exception)
		# Build response:
		response = other_error.get_response()

	# Log ending of request:
	logger.info(_Pauli_Constants.REQUEST_ENDING_MESSAGE)

	# Send response:
	return response















#   ___  ______ _____  ______ _____ _____ _____  ___  ___ _____ _____ _   _ ___________  _____ 
#  / _ \ | ___ \_   _| | ___ \  ___/  ___|_   _| |  \/  ||  ___|_   _| | | |  _  |  _  \/  ___|
# / /_\ \| |_/ / | |   | |_/ / |__ \ `--.  | |   | .  . || |__   | | | |_| | | | | | | |\ `--. 
# |  _  ||  __/  | |   |    /|  __| `--. \ | |   | |\/| ||  __|  | | |  _  | | | | | | | `--. \
# | | | || |    _| |_  | |\ \| |___/\__/ / | |   | |  | || |___  | | | | | \ \_/ / |/ / /\__/ /
# \_| |_/\_|    \___/  \_| \_\____/\____/  \_/   \_|  |_/\____/  \_/ \_| |_/\___/|___/  \____/ 
                                                                                       
# P O S T                      
@app.route(Pauli_project_main_path, methods=['POST'])
def post():

	try:

		rest_method = 'POST'
		# Build request data:
		request_data = json.loads(request.data)
		# Consumes api central function:
		response = api(request_data,rest_method)
		
	# Exception was already handled (i.e. error was built and logged in a deeper except) so error is extracted an response is built
	except Already_Handled_Exception as already_handled_exception:

		# Get inner error:
		inner_error = already_handled_exception.value
		# Build response:
		response = inner_error.get_response()

	# Handle other exception, build error and response:
	except:

		# Get exception
		other_exception = str(sys.exc_info()[1])
		# Build error from exception
		other_error = Error(_Pauli_Constants.HTTP_CODES['INTERNAL'],_Pauli_Constants.ERROR_MESSAGES['INTERNAL'])
		# Log exception/error:
		logger.critical(other_error.content + other_exception)
		# Build response:
		response = other_error.get_response()

	# Send response:
	return response

# G E T
@app.route(Pauli_project_main_dynamic_path, methods=['GET'])
def get(dynamic_path = None):

	try:	
		
		rest_method = 'GET'
		# Build request data
		request_data = {
			'function' : dynamic_path,
			'params' : request.args
		}# End of request data
		# Consumes api central function:
		response = api(request_data,rest_method)
		
	# Exception was already handled (i.e. error was built and logged in a deeper except) so error is extracted an response is built
	except Already_Handled_Exception as already_handled_exception:

		# Get inner error:
		inner_error = already_handled_exception.value
		# Build response:
		response = inner_error.get_response()

	# Handle other exception, build error and response:
	except:

		# Get exception
		other_exception = str(sys.exc_info()[1])
		# Build error from exception
		other_error = Error(_Pauli_Constants.HTTP_CODES['INTERNAL'],_Pauli_Constants.ERROR_MESSAGES['INTERNAL'])
		# Log exception/error:
		logger.critical(other_error.content + other_exception)
		# Build response:
		response = other_error.get_response()

	# Send response:
	return response









#  _____      _                   _____                          
# /  ___|    | |                 /  ___|                         
# \ `--.  ___| |_   _   _ _ __   \ `--.  ___ _ ____   _____ _ __ 
#  `--. \/ _ \ __| | | | | '_ \   `--. \/ _ \ '__\ \ / / _ \ '__|
# /\__/ /  __/ |_  | |_| | |_) | /\__/ /  __/ |   \ V /  __/ |   
# \____/ \___|\__|  \__,_| .__/  \____/ \___|_|    \_/ \___|_|   
#                        | |                                     
#                        |_|   

try:

	if __name__ == '__main__':
		# Define logger:
		logger = _Log.setup_custom_logger('root',_Config)
		logger.info(_Pauli_Constants.STARTING_SERVER + str(Pauli_project_private_port))
		# Set db connection data:
		if 'db' in _Config.general and 'host' in _Config.general['db'] and 'name' in _Config.general['db'] and 'port' in _Config.general['db']:
		 	_Pauli_Helper.DB_NAME = _Config.general['db']['name']
			_Pauli_Helper.DB_PORT = _Config.general['db']['port']
			_Pauli_Helper.DB_HOST = _Config.general['db']['host']
			logger.info(_Pauli_Constants.STABILISH_DB_CONNECTINON + _Pauli_Helper.DB_HOST  + ':' + str(_Pauli_Helper.DB_PORT) + '/' + _Pauli_Helper.DB_NAME)
		# Intialize API	
		app.debug = _Config.general['debugging_available']
		app.run(host='0.0.0.0',threaded=True, port=Pauli_project_private_port)

# Exception was already handled (i.e. error was built and logged in a deeper except) so error is extracted an response is built
except Already_Handled_Exception as already_handled_exception:

	None

# Handle other exception, build error and response:
except:

	# Get exception
	exception = str(sys.exc_info()[1])
	error_message = _Pauli_Constants.STARTING_SERVER_ERROR + exception
	if logger:
		logger.debug(error_message)
	else:
		print error_message
		




