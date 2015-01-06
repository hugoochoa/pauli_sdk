# -*- coding: utf-8 -*-

# ███╗   ██╗███████╗██╗    ██╗    ██████╗  █████╗ ██╗   ██╗██╗     ██╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
# ████╗  ██║██╔════╝██║    ██║    ██╔══██╗██╔══██╗██║   ██║██║     ██║    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
# ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██████╔╝███████║██║   ██║██║     ██║    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
# ██║╚██╗██║██╔══╝  ██║███╗██║    ██╔═══╝ ██╔══██║██║   ██║██║     ██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
# ██║ ╚████║███████╗╚███╔███╔╝    ██║     ██║  ██║╚██████╔╝███████╗██║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
# ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝                                                                                                                                    
                                                                                                                                                     
# DESCRIPTION:
# Create template for a new Pauli project





# ======================================================== DEPENDENCIES

# Native:
import sys
from subprocess import call





# ======================================================== CODE MODULE

try:

	arguments = sys.argv
	if len(arguments) != 3:
		raise Exception('Invalid arguments')

	# Get arguments:
	pauli_project_path = arguments[1]
	pauli_project_folder_name = arguments[2]
	# Command:
	execute_sh_new_project = 'sh /usr/local/lib/pauli_sdk/New/new_project.sh ' + pauli_project_path + ' ' + pauli_project_folder_name


	# Function for execution commands:
	def execute(command):
		command = command.split(' ')
		call(command)

	# Execute installation:
	execute(execute_sh_new_project)

# Handle other exception
except:

	# Get exception:
	exception = str(sys.exc_info()[1])
	# Print exception:
	print 'Error creating Pauli Project: ' + exception








