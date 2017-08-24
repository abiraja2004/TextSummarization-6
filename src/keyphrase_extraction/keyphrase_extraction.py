from weighted_tagbased_phrase_extraction import retrieve_weighted_tagbased_phrase
from collocation import retrieve_top_ngrams_collocations
from src.util.text_normalization_util import normalize_document


# Generate keyphrases
def get_keyphrases(corpus, method='col', number_of_keyphrases=5, phrase_grammar_pattern=r'NP: {<DT>? <JJ>* <NN.*>+}',
                   ngram_size=2):
    if method == 'col':
        norm_corpus = filter(None, normalize_document(corpus, lemmatize=True))
        keyphrases = retrieve_top_ngrams_collocations(corpus=norm_corpus, ngram_size=ngram_size, top=number_of_keyphrases)
        return keyphrases
    elif method == 'wtp':
        keyphrases = retrieve_weighted_tagbased_phrase(corpus=corpus, phrase_grammar_pattern=phrase_grammar_pattern,
                                                       top=number_of_keyphrases)
        return keyphrases
    else:
        raise Exception("Wrong method type entered. Possible values: 'col', 'wtp'")


def print_keyphrases(keyphrases, display_weights=False):
    if display_weights:
        for keyphrase in keyphrases:
            print keyphrase
    else:
        for keyphrase in keyphrases:
            print keyphrase[0]
