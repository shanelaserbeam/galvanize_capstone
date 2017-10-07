#Shane Bryan's Inverted pyramid vectorizer
from collections import defaultdict
import math
import numpy as np
from sklearn.preprocessing import normalize
from scipy import sparse

class IPvectorizer:
    def __init__(self):
        self.words = {}
        self.idf = {}
        self.vocab = set()

    def get_feature_names(self):
        #returns feature names
        return [i for i in self.idf]

    def get_vocab(self, docs):
        #gets the tokens used
        temp_vocab = set()
        for doc in docs:
            doc_vocab = [w for w in doc.split(" ") if len(w) > 1]
            temp_vocab = temp_vocab.union(set(doc_vocab))

        self.vocab = temp_vocab


    def calc_idf(self, docs):
        #implemented using the method found in sklearn
        #will be reworked to utilize hashing to speed up performance
        doc_count = len(docs)
        word_idf = defaultdict(lambda: 0)
        for doc in docs:
            doc_set = set(doc.split(" "))
            for word in doc_set:
                if word in self.vocab:
                    word_idf[word] += 1

        for word in self.vocab:
            #sklearn version
            word_idf[word] = 1+math.log((doc_count+1) / float(1 + word_idf[word]))
            #standard version
            # word_idf[word] = math.log((doc_count) / float(1 + word_idf[word]))
        self.idf = word_idf


    def get_standard_weights(self, doc):
        temp_dict = defaultdict(lambda: 0)
        doc_len = len(doc)
        for w in doc:
            temp_dict[w] += 1. / doc_len
        return temp_dict

    def fit_transform_tfidf(self, docs, status=False):
        #uses tfidf similar to sklearn's version for comparisions
        self.get_vocab(docs)
        self.calc_idf(docs)

        temp_matrix_list = []
        county = 0
        for t in docs:
            doc_word_list = []
            t_words = t.split(" ")
            doc_word_weights = defaultdict(lambda: 0)
            doc_word_weights = self.get_standard_weights(t_words)
            for word in self.idf:
                   doc_word_list.append(doc_word_weights[word] * self.idf[word])
            temp_matrix_list.append(doc_word_list)
            county += 1
            if status and county % 150 == 0:
                print "document {}".format(county)
        temp_array = sparse.csr_matrix(temp_matrix_list)
        return normalize(temp_array, axis=1, norm='l2')

    def transform_tfidf(self, docs):
        #uses tfidf similar to sklearn's version for comparisions

        temp_matrix_list = []
        for t in docs:
            doc_word_list = []
            t_words = t.split(" ")
            doc_word_weights = defaultdict(lambda: 0)
            doc_word_weights = self.get_standard_weights(t_words)
            for word in self.idf:
                   doc_word_list.append(doc_word_weights[word] * self.idf[word])
            temp_matrix_list.append(doc_word_list)
        return normalize(sparse.csr_matrix(temp_matrix_list), axis=1, norm='l2')

    def fit_transform_ip(self, docs, status=False):
        #uses inverted pyramid scaling
        self.get_vocab(docs)
        self.calc_idf(docs)
        temp_matrix_list = []
        county = 0
        for t in docs:
            doc_word_list = []
            t_words = t.split(" ")
            doc_word_weights = defaultdict(lambda: 0)
            doc_word_weights = self.ip_weights(t_words)

            for word in self.idf:
                   doc_word_list.append(1.0* doc_word_weights[word] * self.idf[word])
            temp_matrix_list.append(doc_word_list)
            county += 1
            if status and county % 150 == 0:
                print "document {}".format(county)
        temp_array = sparse.csr_matrix(temp_matrix_list)
        return normalize(temp_array, axis=1, norm='l2')
        # return temp_array

    def transform_ip(self, docs):
        #uses inverted pyramid scaling
        temp_matrix_list = []
        for t in docs:
            doc_word_list = []
            t_words = t.split(" ")
            doc_word_weights = defaultdict(lambda: 0)
            doc_word_weights = self.ip_weights(t_words)

            for word in self.idf:
                   doc_word_list.append(1.0* doc_word_weights[word] * self.idf[word])
            temp_matrix_list.append(doc_word_list)
        return normalize(sparse.csr_matrix(temp_matrix_list), axis=1, norm='l2')

    def ip_weights(self, doc):
        #weights the occurances of tokens in a document by the logrithmic forumula
        temp_dict = defaultdict(lambda: 0)
        doc_len = len(doc)
        county = 0
        for w in doc:
            temp_dict[w] += np.log((doc_len + 1.) / (.1*county + 1))
            county += 1
        return temp_dict
