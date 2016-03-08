import nltk
import pprint as pp
from sklearn import cross_validation
from sklearn import metrics
from nltk.corpus import stopwords
from nltk.stem.porter import *
#from random import shuffle
try:
	import cPickle as pickle
except ImportError:
	import pickle

pickled_file = raw_input('give me the pickled file: \n')
def read_pickled_reviews(pickled_file):
	f = open(pickled_file,'rb')
	data = pickle.load(f)
	f.close()
	return data

# pprint.pprint(read_pickled_reviews()[-1])

def get_words_in_data(data):
	all_words = []
	for words, label in data:
		all_words.extend(words)
	return all_words


def get_word_features(all_words):
	word_freq = nltk.FreqDist(all_words)
	word_features = word_freq.keys()
	return word_features


def extract_features(doc):
	doc_words = set(doc) # get all words unrepeatedly in doc, a doc is a list of words in review.
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in doc_words)
	return features


data  = read_pickled_reviews(pickled_file)
all_words = get_words_in_data(data)
all_words = [w for w in all_words if w.lower() not in stopwords.words('english')]
ps = PorterStemmer()
all_words = map(ps.stem, all_words)
#word_features = get_word_features(all_words)
word_features = list(set(all_words))
print len(word_features)
# pprint.pprint(get_word_features(all_words))

# *********************************
featuresets = [(extract_features(doc),c) for (doc,c) in data]
#featuresets = shuffle(featuresets)
#pp.pprint(featuresets[:1])
#print "lenth of featuresets: ",len(featuresets)
#print "lenth of each feature: ", len(featuresets[0])
#n = int(len(featuresets) * 0.9)
#train_set, test_set = featuresets[:n], featuresets[n:]
cv = cross_validation.KFold(len(featuresets), n_folds = 10, shuffle = False, random_state = None)

for cv_train, cv_test in cv:
	print "start to train a new classifier"
	clf = nltk.NaiveBayesClassifier.train(featuresets[cv_train[0]:cv_train[len(cv_train)-1]])
	print "accuracy: %.5f" % nltk.classify.util. accuracy(clf, featuresets[cv_test[0]:cv_test[len(cv_test)-1]])
	#print clf.show_most_informative_features(10)

#my_nb_clfier = nltk.NaiveBayesClassifier.train(train_set)
#print nltk.classify.accuracy(my_nb_clfier,test_set)
#**********************************