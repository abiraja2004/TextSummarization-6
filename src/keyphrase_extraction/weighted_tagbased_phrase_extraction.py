"""
Key phrase extraction, also known as terminology extraction, is defined as the process or technique of extracting key
    important and relevant terms or phrases from a body of unstructured text such that the core topics or themes of the
    text document(s) are captured in these key phrases.
It can be used in semantic web, query-based search engines, recommendation systems, tagging systems, document
    similarity.
Generally it can be done via two techniques:
    1. Collocation
    2. Weighted tag-based phrase extraction

Weighted tag-based phrase extraction
    1. Extract all known phrases chunks using shallow parsing.
    2. Computer TF-IDF weights for each chunk and then return the top weighted phrases.

"""
import itertools
from operator import itemgetter
from src.util.text_normalization_util import normalize_document, stopword_list
import nltk
from gensim import corpora, models


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
