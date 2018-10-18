#!/usr/local/bin/python3

# ---------------------- IMPORT LIBRARIES ---------------------- #

# -------------------------------------------------------------- #


class Models :
		
		
	@classmethod
	def query_Sites (cls) :
		""" Returns the SQL syntax used to get the list of sites.
		
		:returns string:
		"""
		
		return """
				SELECT * FROM Sites WHERE Active = 1;
		"""
	
	
	@classmethod
	def query_Users (cls) :
		""" Returns the SQL syntax used to get the list of users.
		
		:returns string:
		"""
		
		return """
				SELECT * FROM Users WHERE Active = 1;
		"""
		
		
	@classmethod
	def query_Quotes (cls, quote) :
		""" Returns the SQL syntax used to get the list of quotes.
		
		:param quote: str - The quote to be queried 
		:returns string:
		"""
		
		return """
				SELECT * FROM Quotes WHERE Quote = "%s";
		""" % quote
		
		
	@classmethod
	def insert_Quote (cls, quote, urlId) :
		""" Returns the SQL syntax used to insert a new quote.
		
		:param quote: str - The quote to be inserted 
		:returns string:
		"""
		
		return """
				INSERT INTO Quotes (
					 UrlId
					,Quote
				) VALUES (
					 %s
					,%s
				);
		""" % (urlId, quote)