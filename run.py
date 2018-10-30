# System Module
import numpy as np
import time
import re
import logging
import json
from pprint import pprint
from functools import reduce

# Customized Module
from document_parser import DocumentParser
from sentence_parser import SentenceParser
from dict_module import combineCustomDict, intersectByKeyDict, aveDict, topDict
from tfidf_module import tfidf

logging.basicConfig(filename='log.txt',level=logging.DEBUG,
	format='%(asctime)s:%(levelname)s:%(message)s')

def main():
	# Initialization
	starttime = time.time()
	files     = ["doc%01d.txt" % r for r in range(1,6)]
	docparser = DocumentParser()
	senparser = SentenceParser()

	# Parse the input files into lists of sentences and words
	# And use TF-IDF score to rank each word in a document
	logging.debug('Parsing Documents Into Sentences')
	sentences = []
	doclength = []
	fdict     = {}
	tfdict    = {}
	fidict    = {}

	for num_f,f in enumerate(files):
		logging.debug('Loop Over Document [ {} ]'.format(f))
		for s in docparser.parse(open(f,'r').read()):
			doclength.append(len(s))

			filtersentences=[]

			for num_s,ss in enumerate(s):
				sentences.append(ss)
				for w,newsentence in senparser.parse(ss):
					filtersentences.append(newsentence)
					wdict = senparser.count(SentenceID=num_s, DocID=num_f)
					fdict = combineCustomDict(fdict,wdict)
								
			logging.debug('Perform TF-IDF Analysis for Document [ {} ]'.format(f))
			tfdict = tfidf(filtersentences,top=100)

			fidict = intersectByKeyDict(fidict,tfdict) 
	
	# Find the top word 
	topnumber = 1
	logging.debug('Find the top {} words between all Documents'.format(topnumber))
	topkeys = topDict(fidict, top=topnumber)

	# Output the corresponding Document and Sentence Info
	ftable={}
	doclength.insert(0,0) #insert 0 at the beginning of doclength list
	for tkey in topkeys:
		ftable[tkey] = {}
		#ftable[tkey]['score']= np.mean(fidict[tkey])
		ftable[tkey]['doc']  = np.unique(fdict[tkey]['docid']).tolist()

		for inum,ituple in enumerate(zip(fdict[tkey]['sentenceid'],fdict[tkey]['docid'])):
			senindex=ituple[0]+reduce((lambda x,y: x+y),doclength[:(ituple[1]+1)])
			ftable.setdefault(tkey,{}).setdefault('sentences',[]).append(sentences[senindex])

	print("The Hashtag Table is\n {}".format(json.dumps(ftable,indent=2)),file=open('hashtag_table.txt','w'))

	# Post-Run Analysis
	endtime = time.time()
	logging.debug('Total Runtime: {}'.format(endtime-starttime))



if __name__ == '__main__':
	main()