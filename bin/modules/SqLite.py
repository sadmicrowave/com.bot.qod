#!/usr/local/bin/python3

# ---------------------- IMPORT LIBRARIES ---------------------- #
import sqlite3
# -------------------------------------------------------------- #


class SqLite (object):
	
	''' The SqlLite class is used to interact with SqlLite databases and tables.  This class wrapper interacts with the
	sqlite3 python3 module to create, query, and insert data.
	'''
	
	
	def __init__ (self, sqlite) :
		'''Initialize the class to handle interacting with the SqLite Database.
		
		:param / sqlite: str - The path including the filename of the SqLite3 database object to connect
		:return / .
		:throws / .
		'''
		
		self.conn
		self.curs
		self.sqlite = sqlite
		


	def connect (self) :
		'''Create a new connection to an SqLite database.
		
		:param	/ .
		:return	/ .	
		:throws	/ .
		'''
		
		self.conn = sqlite3.connect( self.sqlite )
		# Set the cursor to interact with the connection
		self.curs = self.conn.cursor()
		
			
		
	def close (self) :
		'''Close the connection to the SqLite object.
		
		:access	/ .
		:param	/ .
		:return	/ .	
		:throws	/ .
		'''
		
		# For good measure, commit changes before closing the session
		self.__commit__()
		
		self.conn.close()
		
		
	def __commit__ (self) :
		'''Use the active SqLite connection to commit data changes to the database.
		
		:param	/ private - class access only
		:return	/ .	
		:throws	/ .
		'''
		
		self.conn.commit()
	
