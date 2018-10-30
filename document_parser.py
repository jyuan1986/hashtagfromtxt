import re
from nltk import sent_tokenize

class DocumentParser:
	def __init__(self):
		self.sentence=[]

	def parse(self,f):
		"""
		parse function converts a string into a list of sentences
		"""
		#Method-1: Regression Splitting
		#self.sentence=re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])',f)

		#Method-2: NLTK Tokenizing
		self.sentence=sent_tokenize(f)

		yield self.sentence
	