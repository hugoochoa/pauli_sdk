# -*- coding: utf-8 -*-

# ██████╗ ███████╗███████╗██████╗  ██████╗ ███╗   ██╗███████╗███████╗
# ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗████╗  ██║██╔════╝██╔════╝
# ██████╔╝█████╗  ███████╗██████╔╝██║   ██║██╔██╗ ██║███████╗█████╗  
# ██╔══██╗██╔══╝  ╚════██║██╔═══╝ ██║   ██║██║╚██╗██║╚════██║██╔══╝  
# ██║  ██║███████╗███████║██║     ╚██████╔╝██║ ╚████║███████║███████╗
# ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝
                                                                   
# DESCRIPTION
# Contains classes that manage a Pauli's project responses.





# ======================================================== DEPENDENCIES

# Native:
import logging

# External:
from flask import json
from flask import make_response
from flask import abort

# Development:
from pauli_sdk.Modules import constants as _Pauli_Constants





# ======================================================== MODULE CODE





# ERROR CLASS
class Error():
	http_code = ''
	content = ''

	# CONSTRUCTOR
	def __init__(self, code, content):
		self.http_code = code
		self.content = content

	# METHOD
	def get_json(self):
		error_json = self.content
		return json.dumps(error_json)

	# METHOD
	def get_type(self):
		return _Pauli_Constants.RESPONSE_TYPES['ERROR']

	# METHOD
	def get_response(self):
		return make_response(self.get_json(),self.http_code)





# SUCCESS CLASS
class Success():
	http_code = 200
	content = ''

	# CONSTRUCTOR
	def __init__(self, content):
		self.content = content

	# METHOD
	def get_json(self):
		success_json = self.content
		return json.dumps(success_json)

	# METHOD
	def get_type(self):
		return _Pauli_Constants.RESPONSE_TYPES['SUCCESS']

	# METHOD
	def get_response(self):
		return make_response(self.get_json(),self.http_code)





# VALIDATING EXCEPTION CLASS:
class Validating_Exception(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)






# GENERAL EXCEPTION CLASS:
class Already_Handled_Exception(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)



		