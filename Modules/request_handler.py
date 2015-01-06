# -*- coding: utf-8 -*-

# ██████╗ ███████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗    ██╗  ██╗ █████╗ ███╗   ██╗██████╗ ██╗     ███████╗██████╗ 
# ██╔══██╗██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝    ██║  ██║██╔══██╗████╗  ██║██╔══██╗██║     ██╔════╝██╔══██╗
# ██████╔╝█████╗  ██║   ██║██║   ██║█████╗  ███████╗   ██║       ███████║███████║██╔██╗ ██║██║  ██║██║     █████╗  ██████╔╝
# ██╔══██╗██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║       ██╔══██║██╔══██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██╔══██╗
# ██║  ██║███████╗╚██████╔╝╚██████╔╝███████╗███████║   ██║       ██║  ██║██║  ██║██║ ╚████║██████╔╝███████╗███████╗██║  ██║
# ╚═╝  ╚═╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                         
# DESCRIPTION:
# Handle requests and function execution of a Pauli's project





# ======================================================== DEPENDENCIES

# Native:
import logging
import sys

# Development:
from pauli_sdk.Modules import constants as _Pauli_Constants
from pauli_sdk.Classes.response import Error
from pauli_sdk.Classes.response import Already_Handled_Exception







# ======================================================== MODULE CODE

logger = logging.getLogger('root')




    #            ██╗      ██████╗ ██╗   ██╗██████╗ ██╗     ██╗ ██████╗     ██████╗ ██████╗ ██████╗ ███████╗
    #            ╚██╗     ██╔══██╗██║   ██║██╔══██╗██║     ██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
    # █████╗█████╗╚██╗    ██████╔╝██║   ██║██████╔╝██║     ██║██║         ██║     ██║   ██║██║  ██║█████╗  
    # ╚════╝╚════╝██╔╝    ██╔═══╝ ██║   ██║██╔══██╗██║     ██║██║         ██║     ██║   ██║██║  ██║██╔══╝  
    #            ██╔╝     ██║     ╚██████╔╝██████╔╝███████╗██║╚██████╗    ╚██████╗╚██████╔╝██████╔╝███████╗
    #            ╚═╝      ╚═╝      ╚═════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝




    
def execute(valid_request_data,_pauli_project_config_file):

    try:

        # Get validated params:
        function_called = valid_request_data['function']
        validated_function_params = valid_request_data['params']
        # Get execution data:
        function_called_instance = _pauli_project_config_file.functions[function_called]['instance']
        # Execution:
        logger.info(_Pauli_Constants.EXECUTING_REQUEST_MESSAGE + function_called)
        function_result = function_called_instance(validated_function_params)
        return function_result

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
                                                                                                                  




# There are not private code                                                                                                                  



