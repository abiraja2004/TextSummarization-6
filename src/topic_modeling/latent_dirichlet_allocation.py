"""
Generative probabilistic model where each document is assumed to have a combination of topics similar to a
    probabilistic latent semantic indexing model, but in this case, the latent topics contain a Dirichlet prior over
    them.
"""
from gensim import models
from preprocessing import preprocess


def train_lda_model(corpus, total_topics=2):
    corpus_tfidf, dictionary = preprocess(corpus=corpus)

    lda = models.LdaModel(corpus_tfidf, id2word=dictionary, iterations=1000, num_topics=total_topics)

    return lda
