#!/usr/local/bin/python3

# ---------------------- IMPORT LIBRARIES ---------------------- #
import os, logging

from logging import handlers
from logging.config import dictConfig

from SqLite import SqLite
# -------------------------------------------------------------- #

class Environment :
	""" The Environment class defines and creates the directory structures necessary for the output
	files from this program including actual file delivery directory, archive dir, any temp dirs 
	needed for file moves, and log directory and file creation.  The class is also responsible
	for instantiating the log handler/rotator for log outputs and ensuring the sqlite database is
	setup.
	"""
	
	__log = None
	
	# This is the class constructor, it will get executed automatically when the class is instantiated
	def __init__ (self, **kwargs) :
		# assign class variables using kwargs dict
		for name, value in kwargs.items():
			# Make each keyword-argument a property of the class.
			setattr(self, name, value)
		
		# call the method to setup the log, do this first so all other proceeding actions end up with
		# a valid log file to write to, in the event of an issue, etc.
		self.__setupLog( self.name )
		
		self.__seupDB( self.name )

	
	def __setupDB (self, name) :
		# Set the path and filename to the sqlite3 database
		sqlite = os.path.join(self.db_dir, "%s.sqlite3" % name)
		
		sql = SqLite( sqlite )
		sql.connect()
		
		sql.curs.execute("""
						CREATE TABLE IF NOT EXISTS Users (
							 Id				INTEGER PRIMARY KEY
							,UrlId			INTEGER NOT NULL
							,Phone			TEXT NOT NULL
							,SentCount		SIGNED INT DEFAULT 0
							,Active			NUMERIC DEFAULT 1
							,Created		DATETIME DEFAULT current_timestamp
						);
						
						CREATE TABLE IF NOT EXISTS Sites (
							 Id			INTEGER PRIMARY KEY
							,Url		TEXT NOT NULL
							,Active		NUMERIC DEFAULT 1
							,Created	DATETIME DEFAULT current_timestamp
						);

                        CREATE TABLE IF NOT EXISTS Subscribed (
                             Id         INTEGER PRIMARY KEY
                            ,UserId     INTEGER NOT NULL
                            ,SiteId     INTEGER NOT NULL
                            ,DOW        TEXT NOT NULL 
                                # The DOW field format is as follows: weekday (0-6, 0 = Sunday, * = Everyday).
                                # Ranges can be used as: 1-5 = Monday through Friday
   
                            ,Time       NUMERIC DEFAULT 800
                                # Time field is numeric (no alpha characters allowed). 
                                # Time format is in 24 hr format, no colon: e.g. 800 = 8:00 AM, 2300 = 11:00 PM

                            ,Created    DATETIME DEFAULT current_timestamp
                        );
							
						CREATE TABLE IF NOT EXISTS Quotes (
							 Id			INTEGER PRIMARY KEY
							,UrlId		INTEGER NOT NULL
							,Quote		TEXT NOT NULL
							,Created	DATETIME DEFAULT current_timestamp
						);

						""")
		
		
	
	
	
	def __setupLog (self, name) :
		# Try/Catch best practice says not to embed try/catch blocks inside methods themselves, but instead place them around the calling operation
		# where the method is actually called.  We drift away from best practice here because we need an internal exception handler to tell the program
		# what to do in the event the log can't be created, since the outer-most bubbled try/catch still attempts to use the log variable, yet it might not
		# get successfully created here, we need an alternative action to execute, like raising the exception to the screen for the user. 
		try:
			# Create the logger config dictionary, this is a simple JSON array which is loaded into
			# the log module and used to configure the python logger with the option we want.
			LOG_SETTINGS = {	 
								 'version' : 1
								,'handlers': {
												'core': {
															 # make the logger a rotating file handler so the file automatically gets archived and a new one gets created, preventing files
															 # from becoming too large they are unmaintainable. 
															 'class'		: 'logging.handlers.RotatingFileHandler'
															 # by setting our logger to the DEBUG level (lowest level) we will include all other levels by default
															,'level'		: 'DEBUG'
															 # this references the 'core' handler located in the 'formatters' dict element below
															,'formatter'	: 'core'
															 # the path and file name of the output log file
															,'filename' 	: os.path.join(self.log_dir, "%s.log" % name)
															,'mode'			: 'a'
															 # the max size we want to log file to reach before it gets archived and a new file gets created
															,'maxBytes'		: 100000
															 # the max number of files we want to keep in archive
															,'backupCount' 	: 5
												}
								}
								 # create the formatters which are referenced in the handlers section above
								,'formatters': {
												'core': {
															'format': '%(levelname)s %(asctime)s %(module)s|%(funcName)s %(lineno)d: %(message)s' 
												}
								}
								,'loggers'	 : {
												'root': {
															 'level' 	: 'DEBUG' # The most granular level of logging available in the log module
															,'handlers'	: ['core']
												}
								}
							}
		
			# use the built-in logger dict configuration tool to convert the dict to a logger config
			dictConfig(LOG_SETTINGS)
			
			# get the logger created in the config and named root in the 'loggers' section of the config
			self.__log = logging.getLogger('root')
			
			self.__log.info( "*** LOG HANDLER INITIALIZED. ***" )

		
		except Exception as e:
			# since we don't have an active log to put any output messages in, we need to raise/bubble the exception
			# to the outer-most try/catch and let THAT catch tell the program what to do with the error message
			raise 
		

	@property
	def log (self):
		return self.__log