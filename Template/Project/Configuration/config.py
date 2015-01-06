# -*- coding: utf-8 -*-

#  ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ ██╗   ██╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
# ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ ██║   ██║██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
# ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗██║   ██║██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║
# ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║██║   ██║██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
# ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                                                         
                                                                      
# DESCRIPTION:
# Contains Pauli's project main data and api functions:




# ======================================================== DEPENDENCIES

# Development:
from pauli_sdk.Modules import constants as _PAULI_Constants
from Modules import some_module as _Some_Module






# ======================================================== MODULE CODE

# Params validation properties:
list_item_specification = _PAULI_Constants.LIST_ITEM_SPECIFICATION
dict_item_specification = _PAULI_Constants.DICT_ITEM_SPECIFICATION
required_params = _PAULI_Constants.REQUIRED_PARAMS
value_type = _PAULI_Constants.VALUE_TYPE
param_type = _PAULI_Constants.PARAM_TYPE
obligatory = _PAULI_Constants.OBLIBATORY_PARAM
optional = _PAULI_Constants.OPTIONAL_PARAM
instance = _PAULI_Constants.INSTANCE
private_API_key = _PAULI_Constants.PRIVATE_API_KEY
public_function = _PAULI_Constants.PUBLIC_FUNCTION
private_function = _PAULI_Constants.PRIVATE_FUNCTION	




    #            ██╗      ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██████╗  █████╗ ████████╗ █████╗ 
    #            ╚██╗     ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
    # █████╗█████╗╚██╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║  ██║███████║   ██║   ███████║
    # ╚════╝╚════╝██╔╝    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ██║  ██║██╔══██║   ██║   ██╔══██║
    #            ██╔╝     ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ██████╔╝██║  ██║   ██║   ██║  ██║
    #            ╚═╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                                       





# Pauli's project general configuration:
general = {
	# Project name:
	'project_name' : 'SOMBRA',# Our project name
	# Logging data:
	'logging_root' : '/Users/Hugo/Documents/CTAM/CoreBook/Desarrollos/Pauli SDK/Pauli V1.0/app_v1.0/Logs',# Where to log (absolute path)
	'logging_file_default_name' : 'API.log',# Logging file name (justa a file name with .log extension)
	# Listening data:
	'pauli_project_private_port' : 5000,# Our project is gonna be listening on this port (a number)
	'main_path' : '/sombra',# Our project is gonna be listening on this path (/something)
	# Debugging:
	'debugging_available' : True,# If set, every change on the project is gonna be updated (a boolean)
	# DB connection (MongoDB)
	'db' : {
		'host' : 'wallstreetmx.cloudapp.net',# Domain of our DB
		'port' : 27017,# DB port (a number)
		'name' : 'Pauli'# Mongo data base name
	},# End of db
	# Private API key:
	private_API_key : '*_Some_Private_API_Key_'# Use in case of a private API function to authenticate
}# Endo of general












    #            ██╗       █████╗ ██████╗ ██╗    ███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
    #            ╚██╗     ██╔══██╗██╔══██╗██║    ██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
    # █████╗█████╗╚██╗    ███████║██████╔╝██║    █████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
    # ╚════╝╚════╝██╔╝    ██╔══██║██╔═══╝ ██║    ██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
    #            ██╔╝     ██║  ██║██║     ██║    ██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
    #            ╚═╝      ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                                                                         
# Types: list, dict, int, float, unicode (str), bool

# Set of API functions information:
functions = {

	# ██████╗ ██╗   ██╗██████╗ ██╗     ██╗ ██████╗
	# ██╔══██╗██║   ██║██╔══██╗██║     ██║██╔════╝
	# ██████╔╝██║   ██║██████╔╝██║     ██║██║     
	# ██╔═══╝ ██║   ██║██╔══██╗██║     ██║██║     
	# ██║     ╚██████╔╝██████╔╝███████╗██║╚██████╗
	# ╚═╝      ╚═════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝
                                            
	# PUBLIC FUNCTION EXAMPLE:
	'our_public_function' : {
		# Function information:
		public_function : True,
		required_params : {# Required params is a "dict_item_specification"
			'param_1' : { 
				value_type : dict,
				param_type : obligatory,
				dict_item_specification : {
					'inner_param_1' : {
						value_type : unicode,
						param_type : obligatory
					},# End of inner_param_2
					'inner_param_2' : {
						value_type : int,
						param_type : obligatory
					}# End of inner_param_2
				}# End of dict_item_specification 
			},# End of param_1
			'param_2' : { 
				value_type : list,
				param_type : obligatory,
				list_item_specification : {
					value_type : unicode,
					param_type : obligatory
				}
			}# End of param_"
		},# End of required params
		instance : _Some_Module.our_public_function_instance
	},# End of our_public_function






	# ██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ████████╗███████╗
	# ██╔══██╗██╔══██╗██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝
	# ██████╔╝██████╔╝██║██║   ██║███████║   ██║   █████╗  
	# ██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝  
	# ██║     ██║  ██║██║ ╚████╔╝ ██║  ██║   ██║   ███████╗
	# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝                                      
                                                                            
	# PRIVATE FUNCTION EXAMPLE:
	'our_private_function' : {
		# Function information:
		private_function : True,
		required_params : {
			private_API_key : {
				value_type : unicode,
				param_type : obligatory
			}# End of private_API_key
		},# End of required params
		instance : _Some_Module.our_private_function_instance
	},# End of our_private_function

}# End of functions







