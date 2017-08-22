# Key phrase extraction, also known as terminology extraction, is defined as the process or technique of extracting key
# important and relevant terms or phrases from a body of unstructured text such that the core topics or themes of the
# text document(s) are captured in these key phrases.
from operator import itemgetter
import nltk
import itertools
from text_normalization_util import normalize_document
# Bigrams collocations
from nltk.collocations import BigramCollocationFinder
from nltk.collocations import BigramAssocMeasures
# Trigrams collocations
from nltk.collocations import TrigramCollocationFinder
from nltk.collocations import TrigramAssocMeasures
# Weighted Tag-Based Phrase Extraction
from gensim import corpora, models


stopword_list = nltk.corpus.stopwords.words('english')


def flatten_corpus(corpus):
    return ' '.join([sentence.strip() for sentence in corpus])


def compute_ngrams(input, ngram_size):
    return zip(*[input[index:] for index in range(ngram_size)])


def retrieve_top_ngrams_collocations(corpus, ngram_size=1, top=5):
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


def extract_grammar_phrases(corpus, phrase_grammar_pattern):
    # build phrase list based on grammar pattern
    all_phrases = []
    grammar_pattern = nltk.chunk.regexp.RegexpParser(phrase_grammar_pattern)

    sentences = normalize_document(corpus, esc_html=False, expand_cont=False, lemmatize=False, tokenize=False,
                                   remove_special_char=False, remove_stop_words=False)
    for sentence in sentences:
        # POS tag sentences
        tagged_sentences = nltk.pos_tag_sents([nltk.word_tokenize(sentence)])

        # extract phrases based on pattern
        phrases = [grammar_pattern.parse(tagged_sentence) for tagged_sentence in tagged_sentences]

        # extract word, pos tag, tag triples
        wtc_sentences = [nltk.chunk.tree2conlltags(phrase) for phrase in phrases]
        flattened_phrases = list(itertools.chain.from_iterable(wtc_sentence for wtc_sentence in wtc_sentences))

        # get valid phrase based on tags
        valid_phrases_tagged = [(status, [wtc for wtc in chunk])
                                for status, chunk
                                in itertools.groupby(flattened_phrases, lambda (word, pos, chunk): chunk != 'O')]

        valid_phrases = [' '.join(word.lower() for word, tag, chunk in wtc_group if word.lower() not in stopword_list)
                                 for status, wtc_group in valid_phrases_tagged if status]

        all_phrases.append(valid_phrases)

    return all_phrases


def retrieve_weighted_tagbased_phrase(corpus, phrase_grammar_pattern=r'NP: {<DT>? <JJ>* <NN.*>+}', top=5):
    phrases = extract_grammar_phrases(corpus, phrase_grammar_pattern)
    # build tf-idf based model
    dictionary = corpora.Dictionary(phrases)
    corpus = [dictionary.doc2bow(phrase) for phrase in phrases]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    # get phrases and their tf-idf weights
    weighted_phrases = {dictionary.get(id): round(value, 3) for doc in corpus_tfidf for id, value in doc}
    weighted_phrases = sorted(weighted_phrases.items(), key=itemgetter(1), reverse=True)

    return weighted_phrases[:top]