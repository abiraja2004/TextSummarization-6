"""
Correlates and find semantically linked terms from corpora. Besides text summarization, it can be used for search and
    retrieval.
The idea here is that terms tend to be used in the same context and hence tend to co-occur more. This technique has
    the ability to uncover latent (hidden) terms which correlate semantically to form topics
"""
from gensim import corpora, models
from src.util.text_normalization_util import normalize_document


def train_lsi_model(corpus, total_topics=2):
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

    # Build the topic model
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=total_topics)

    return lsi


# Display the generated topics
def print_topics(corpus, total_topics=1, weight_threshold=0.0001, display_weights=False, num_terms=None):
    topic_model = train_lsi_model(corpus, total_topics)

    for index in range(total_topics):
        topic = topic_model.show_topic(index)
        topic = [(word, round(wt, 2))
                 for word, wt in topic
                 if abs(wt) >= weight_threshold]
        if display_weights:
            print 'Topic #' + str(index + 1) + ' with weights'
            print topic[:num_terms] if num_terms else topic
        else:
            print 'Topic #' + str(index + 1) + ' without weights'
            tw = [term for term, wt in topic]
            print tw[:num_terms] if num_terms else tw
        print
