import nltk
import pprint
try:
	import cPickle as pickle
except ImportError:
	import pickle

def read_pickled_reviews():
	f = open('pickled_all_reviews','rb')
	data = pickle.load(f)
	f.close()
	return data

print read_pickled_reviews()[:3]


