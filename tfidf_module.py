import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf(corpus, top=None):
	"""
	tfdif function returns a dictionary of (words, tdidf_score) pairs
	"""
	vectorizer=TfidfVectorizer()
	X   = vectorizer.fit_transform(corpus)
	keys= vectorizer.get_feature_names()
	values=np.asarray(X.mean(axis=0)).flatten()

	mydict=dict(zip(keys,values))
	if top is None:
		return mydict
	else:
		newdict={}
		count=0
		for key, value in sorted(mydict.items(), reverse=True, key=lambda item: (item[1], item[0])):
			if count < top:
				newdict[key]=value
				count+=1
		return newdict