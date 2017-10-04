# import re
#
# from nltk.tokenize import RegexpTokenizer
# from nltk.corpus.util import LazyCorpusLoader
# from nltk.corpus.reader import CategorizedPlaintextCorpusReader
# from nltk import word_tokenize
# from nltk.stem.porter import PorterStemmer
# from nltk.corpus import stopwords
# import re

# cachedStopWords = stopwords.words("english")

def train_test_split(min=25):
    import re

    from nltk.tokenize import RegexpTokenizer
    from nltk.corpus.util import LazyCorpusLoader
    from nltk.corpus.reader import CategorizedPlaintextCorpusReader
    reuters = LazyCorpusLoader(
    'reuters', CategorizedPlaintextCorpusReader, '(training|test).*',
    cat_file='cats.txt', encoding='ISO-8859-2')

    documents = reuters.fileids()

    train_docs_id = list(filter(lambda doc: doc.startswith("train"),
                                documents))
    test_docs_id = list(filter(lambda doc: doc.startswith("test"),
                               documents))

    train_docs = [reuters.raw(doc_id) for doc_id in train_docs_id]
    test_docs = [reuters.raw(doc_id) for doc_id in test_docs_id]
    train_cat = [reuters.categories(doc_id) for doc_id in train_docs_id]
    test_cat = [reuters.categories(doc_id) for doc_id in test_docs_id]

    train_token_docs = []
    train_token_docs_length = []
    train_token_docs_unique = []
    for i in train_docs:
        tempy_tokens = tokenize(i)
        train_token_docs.append(" ".join(tempy_tokens))
        train_token_docs_length.append(len(tempy_tokens))
        train_token_docs_unique.append(len(set(tempy_tokens)))

    test_token_docs = []
    test_token_docs_length = []
    test_token_docs_unique = []
    for i in test_docs:
        tempy_tokens = tokenize(i)
        test_token_docs.append(" ".join(tempy_tokens))
        test_token_docs_length.append(len(tempy_tokens))
        test_token_docs_unique.append(len(set(tempy_tokens)))

    train_less_than_min = [n for n,i in enumerate(train_token_docs_length) if i < min]
    test_less_than_min = [n for n,i in enumerate(test_token_docs_length) if i < min]

    train_token_docs_more_than_min = [i for n,i in enumerate(train_token_docs) if n not in train_less_than_min]

    test_token_docs_more_than_min = [i for n,i in enumerate(test_token_docs) if n not in test_less_than_min]
    train_cat_more_than_min = [i for n,i in enumerate(train_cat) if n not in train_less_than_min]
    test_cat_more_than_min = [i for n,i in enumerate(test_cat) if n not in test_less_than_min]

    #getting single cats
    cat_count_train = [len(i) for i in train_cat_more_than_min]
    cat_count_test = [len(i) for i in test_cat_more_than_min]

    single_cat_train = [n for n,i in enumerate(cat_count_train) if i == 1]
    single_cat_test = [n for n,i in enumerate(cat_count_test) if i == 1]

    train_single = [i for n,i in enumerate(train_token_docs_more_than_min) if n in single_cat_train]
    test_single = [i for n,i in enumerate(test_token_docs_more_than_min) if n in single_cat_test]
    train_single_cat = [i for n,i in enumerate(train_cat_more_than_min) if n in single_cat_train]
    test_single_cat = [i for n,i in enumerate(test_cat_more_than_min) if n in single_cat_test]

    train_cat_set = set([i[0] for i in train_single_cat])
    test_cat_set = set([i[0] for i in test_single_cat])

    mutual_cat = train_cat_set.intersection(test_cat_set)

    member_of_mutual_test = [n for n,i in enumerate(test_single_cat) if i[0] in mutual_cat]
    member_of_mutual_train = [n for n,i in enumerate(train_single_cat) if i[0] in mutual_cat]

    train_single2 = [i for n,i in enumerate(train_single) if n in member_of_mutual_train]
    test_single2 = [i for n,i in enumerate(test_single) if n in member_of_mutual_test]
    train_single_cat2 = [i for n,i in enumerate(train_single_cat) if n in member_of_mutual_train]
    test_single_cat2 = [i for n,i in enumerate(test_single_cat) if n in member_of_mutual_test]

    return train_single2, train_single_cat2, test_single2, test_single_cat2

def tokenize(text):
    from nltk import word_tokenize
    from nltk.stem.porter import PorterStemmer
    from nltk.corpus import stopwords
    import re

    cachedStopWords = stopwords.words("english")
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text))
    words = [word for word in words if word not in cachedStopWords]
    tokens = (list(map(lambda token: PorterStemmer().stem(token),
                                   words)))
    p = re.compile('[a-zA-Z]+');
    filtered_tokens = \
    list(filter (lambda token: p.match(token) and \
                               len(token) >= min_length,tokens))
    #filtered_tokens2 = [strip_accents(i) for i in filtered_tokens]
    return filtered_tokens
