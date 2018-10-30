import re
import string
import collections
from nltk import word_tokenize
from nltk.corpus import stopwords 

class SentenceParser():
	def __init__(self):
		self.words=[]
		self.sentence=''

	def parse(self, f):
		"""
		parse function converts a sentence f (in STRING) into a list of words (in LIST)
		"""
		# Method-1: Regression Split
		#self.words=re.split(f)
		
		# Method-2: NLTK Word_Tokenize
		# Remove Punctionations, Stopwords, Addition_words and lower all words
		stop_words = set(stopwords.words('english')) 
		addition_words = ['\'ve','\'s','n\'t','let','us','know','together','re','must','one']
		self.words=[ w.lower() for w in word_tokenize(f) if not w.lower() in string.punctuation 
			and not w.lower() in stop_words and not w.lower() in addition_words]
		self.sentence=' '.join(self.words)

		yield self.words, self.sentence

	def count(self, SentenceID=None, DocID=None):
		"""
		count function returns a dictionary 
		1) with {word_name: number_of_count} as key-value pair when SentenceID is None
		2) with {word_name : {count: number_of_count, sentenceid: SentenceID, docid: DocID}} when SentenceID is Not None
		"""
		cdict=dict(collections.Counter(self.words))
		if SentenceID is None and DocID is None:
			return cdict
		else:
			result={}
			for key, value in cdict.items():
				result[key]={'count':value,'sentenceid':SentenceID, 'docid': DocID}
			return result


