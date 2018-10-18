#!/usr/local/bin/python3

# The following section is neccesary in order for DocOpt command line argument parsing module to operate
# Do not change the following syntax unless you are familiar with DocOpt specifications.

"""QOD Bot is a python CLI utility designed to gather randomized quotes of the day from websites and distribute to recipients via SMS. 

Usage:
	bot.py [-h | --help]
	bot.py [-v | --verbose]
	bot.py --version

Options:
	-h,--help	: show this help message
	-v,--verbose    : display/log more text output
	--version	: show version
"""

# --------------------------- META ----------------------------- #

__scriptname__	= "Quote of the Day"
__author__ 		= "Corey Farmer"
__copyright__ 	= "Copyright 2018"
__credits__ 	= []
__license__ 	= "GPL"
__version__ 	= "1.0.0"
__maintainer__ 	= "Corey Farmer"
__email__ 		= "corey.m.farmer@gmail.com"


# ----------------------- LOGIC MAPPING ------------------------ #

# 	Command Line Interface Execution
#		|
#		|-> Parse Command Line Arguments with DocOpt module
#		|-> Instantiate ExceptionHandler Class
#		|-> Instantiate Environment Class
#		|	|
#		|	|-> Create and setup log object
#		|	|-> Create/Setup db and table schema
#		|-> 
#		|-> 
#		|-> End program



# ---------------------- IMPORT LIBRARIES ---------------------- #
import os, sys, re, time, urlencode, requests

from docopt import docopt
from bs4 import BeautifulSoup

from bin.modules.Exceptions import ExceptionHandler
from bin.modules.Environment import Environment
from bin.modules.SqLite import SqLite
from bin.models.Models import Models


# -------------------------------------------------------------- #


class Bot :
	""" Bot Cerebral Cortex - main processing core for all bot logic
	and operations.  
	"""
	
	def __init__ (self) :
		pass
		
	
	def getUserList (self) :
		pass
		
	
	def hasActiveUsers (self, ul) :
		pass 
		
		
	def getSites (self) :
		pass
		
		
	def hasActiveSites (self, sl) :
		pass






if __name__ == "__main__":
	
	# Docopt will check all arguments, and exit with the Usage string if they don't pass.
	# If you simply want to pass your own modules documentation then use __doc__,
	# otherwise, you would pass another docopt-friendly usage string here.
	# You could also pass your own arguments instead of sys.argv with: docopt(__doc__, argv=[your, args])
	
	docopt_args = docopt(__doc__, version='QOD Bot 1.0.0')			
	verbosity 	= docopt_args["-v"] or docopt_args["--verbose"]
	listen 		= True
	e 			= None
	
	try:		
		# ----------------- Instantiate the ExceptionHandler object instance in order to add  -----------------  #
		#exceptions to the buffer for emailing later.
		exceptionHandler = ExceptionHandler()
		
		# ----------------- Instantiate the environment class, passing the kwargs we defined -------------------- # 
		# Create a keyword argument dictionary holding the main params we want to use throught the program defining
		# important things like where we want the files to end, etc.
		kwargs = {	
					"name"				: 'com.qod.bot'
					,"log_dir"			: os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'var', 'log')
					,"db_dir"			: os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'var', 'db')
					,"verbose" 			: verbosity
				 }
		e = Environment(**kwargs)


		





				
	except Exception:
	
		if e and e.log : 
			e.log.exception( sys.exc_info()[0] )
			
		raise 
	
	finally :
	
		# if the environment object variable still exists then utilize the log object variable to add an exception entry to the log, since we can't email it apparently
		if e and e.log : 	
			e.log.info( '*** PROGRAM EXITING. ***\n' )
		
		
		
		