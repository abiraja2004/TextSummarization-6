"""
Key phrase extraction, also known as terminology extraction, is defined as the process or technique of extracting key
    important and relevant terms or phrases from a body of unstructured text such that the core topics or themes of the
    text document(s) are captured in these key phrases.
It can be used in semantic web, query-based search engines, recommendation systems, tagging systems, document
    similarity.
Generally it can be done via two techniques:
    1. Collocation
    2. Weighted tag-based phrase extraction

Collocation
    Sequence or group of words that tend to occur frequently such that this frequency tends to be moe than what could
    be terms as a random.
    1. Start with a corpus of documents.
    2. Tokenize them to form sentences.
    3. Flatten the list of sentences to form one large sentence or string.
    4. Slide a window of size n based on the n-gram range, and compute n-grams across the string.
    5. Count each n-gram based on its frequency of occurrences.
    6. Rank n-grams based on their frequency.

"""
from operator import itemgetter
import nltk
from nltk.collocations import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder
from nltk.collocations import TrigramAssocMeasures
from nltk.collocations import TrigramCollocationFinder


def flatten_corpus(corpus):
    return ' '.join([sentence.strip() for sentence in corpus])


def compute_ngrams(input, ngram_size):
    return zip(*[input[index:] for index in range(ngram_size)])


def retrieve_top_ngrams_collocations(corpus, ngram_size=2, top=5):
    corpus = flatten_corpus(corpus)
    tokens = nltk.word_tokenize(corpus)
    ngrams = compute_ngrams(tokens, ngram_size)
    ngrams_freq_dist = nltk.FreqDist(ngrams)
    sorted_ngrams_fd = sorted(ngrams_freq_dist.items(), key=itemgetter(1), reverse=True)
    sorted_ngrams = sorted_ngrams_fd[0:top]
    sorted_ngrams = [(' '.join(text), freq) for text, freq in sorted_ngrams]

    return sorted_ngrams


def retrieve_top_bigrams_collocations(corpus, top=5, measure='pmi'):
    finder = BigramCollocationFinder.from_documents([item.split() for item in corpus])
    bigram_measures = BigramAssocMeasures()

    if measure == 'pmi':
        top_bigrams = finder.nbest(bigram_measures.pmi, top)
    elif measure == 'frequency':
        top_bigrams = finder.nbest(bigram_measures.raw_freq, top)
    else:
        raise ValueError('Type of measure is unknown!')

    return top_bigrams


def retrieve_top_trigrams_collocations(corpus, top=5, measure='pmi'):
    finder = TrigramCollocationFinder.from_documents([item.split() for item in corpus])
    trigram_measures = TrigramAssocMeasures()

    if measure == 'pmi':
        top_trigrams = finder.nbest(trigram_measures.pmi, top)
    elif measure == 'frequency':
        top_trigrams = finder.nbest(trigram_measures.raw_freq, top)
    else:
        raise ValueError('Type of measure is unknown!')

    return top_trigrams

