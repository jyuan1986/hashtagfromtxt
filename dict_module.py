"""
Module for Maninpulating Dictionaries
"""
import numpy as np

def combineDict(*args):
	"""
	Combine Multiple (One-Level) Dictionaries into a Dictionary
	"""
	result = {}
	for dic in args:
		for key in (result.keys() | dic.keys()):
			if key in dic:
				if type(dic[key]) is list:
					result.setdefault(key, []).extend(dic[key])
				else:
					result.setdefault(key, []).append(dic[key])
	return result


def intersectByKeyDict(*args):
	"""
	Obtain pairs with the same key values of Multiple (One-Level) Dictionaries into a dictionary
	"""
	result = {}
	for dic in args:
		if not bool(result):
			for key in dic.keys():
				if type(dic[key]) is list:
					result.setdefault(key, []).extend(dic[key])
				else:
					result.setdefault(key, []).append(dic[key])				
		else:
			for key in (result.keys() | dic.keys()):
				if key in (result.keys() & dic.keys()):
					if type(dic[key]) is list:
						result.setdefault(key, []).extend(dic[key])
					else:
						result.setdefault(key, []).append(dic[key])		
				else:
					result.pop(key,None)
	return result



def sumDict(dictionary):
	"""
	Sum over value of keys in a (One-Level) dictionary
	"""
	result={}
	for key,lis in dictionary.items():
		result[key]=sum(lis)
	return result

def aveDict(dictionary):
	"""
	Sum over value of keys in a (One-Level) dictionary
	"""
	result={}
	for key,lis in dictionary.items():
		result[key]=np.mean(lis)
	return result


def topDict(dictionary,top=1):
	"""
	Output the key with top N values in a dictionary
	"""
	result = []
	meandict=aveDict(dictionary)
	count = 0
	for key, value in sorted(meandict.items(), reverse=True, key=lambda item: (item[1], item[0])):
		if count < top:
			result.append(key)
			count+=1
	return result


def combineCustomDict(*args):
	"""
	Combine Multiple (Two-Level Customized) Dictionaries into a Dictionary
	"""
	#{word_name : 
	#            {count: number_of_count, 
	#             sentenceid: SentenceID, 
	#             docid: DocID
	#            }
	#}
	result = {}
	for dic in args:
		for key in (result.keys() | dic.keys()):
			if key in dic:
				
				# 1. Aggregate Count Value
				result.setdefault(key,{})['count'] = result.setdefault(key,{}).setdefault('count',0)+dic[key]['count']

				# 2. Concatenate sentenceid and docid value (removind duplicates)
				if type(dic[key]['sentenceid']) is list:
					result.setdefault(key,{}).setdefault('sentenceid',[]).extend(dic[key]['sentenceid'])
				else:
					result.setdefault(key,{}).setdefault('sentenceid',[]).append(dic[key]['sentenceid'])

				if type(dic[key]['docid']) is list:
					result.setdefault(key,{}).setdefault('docid',[]).extend(dic[key]['docid'])
				else:
					result.setdefault(key,{}).setdefault('docid',[]).append(dic[key]['docid'])
				
	return result