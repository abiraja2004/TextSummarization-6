"""
Correlates and find semantically linked terms from corpora. Besides text summarization, it can be used for search and
    retrieval.
The idea here is that terms tend to be used in the same context and hence tend to co-occur more. This technique has
    the ability to uncover latent (hidden) terms which correlate semantically to form topics
"""
from gensim import models
from preprocessing import preprocess


def train_lsi_model(corpus, total_topics=2):
    corpus_tfidf, dictionary = preprocess(corpus=corpus)

    # Build the topic model
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=total_topics)

    return lsi
