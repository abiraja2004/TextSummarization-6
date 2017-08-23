from gensim import corpora, models
from src.util.text_normalization_util import normalize_document


def preprocess(corpus):
    # normalize text
    normalized_document = normalize_document(corpus, tokenize=True)

    # Build a dictionary, which gensim uses to map each unique term into a numeric value
    dictionary = corpora.Dictionary(normalized_document)

    # Using built dictionary, convert normalized text into a numeric Bag of Words vector representation. Each term and
    # its frequency in a sentence is depicted by a tuple(term, frequency)
    mapped_corpus = [dictionary.doc2bow(text) for text in normalized_document]

    # Build a TF-IDF-weighted model over corpus where each term in each document will contain its TF-IDF weight.
    tfidf = models.TfidfModel(mapped_corpus)
    corpus_tfidf = tfidf[mapped_corpus]

    return corpus_tfidf, dictionary


