"""
Matrix decomposition similar to SVD that seems to work better that LSI and LDA even with small corpora.
"""
from sklearn.decomposition import NMF
from src.util.text_normalization_util import normalize_document
from src.util.feature_extraction_util import build_feature_matrix
import numpy as np


def train_nmf_model(corpus, total_topics=2):
    # normalize text
    normalized_document = normalize_document(corpus)

    vectorizer, tfidf_matrix = build_feature_matrix(normalized_document, feature_type='tfidf')

    # build topic model
    nmf = NMF(n_components=total_topics, random_state=42, alpha=.1, l1_ratio=.5)
    nmf.fit(tfidf_matrix)

    return nmf, vectorizer


def get_topics_terms_weights(nmf, vectorizer):
    # get terms and their weights
    feature_names = vectorizer.get_feature_names()
    weights = nmf.components_

    feature_names = np.array(feature_names)
    sorted_indices = np.array([list(row[::-1])
                               for row
                               in np.argsort(np.abs(weights))])
    sorted_weights = np.array([list(wt[index])
                               for wt, index
                               in zip(weights, sorted_indices)])
    sorted_terms = np.array([list(feature_names[row])
                             for row
                             in sorted_indices])

    topics = [np.vstack((terms.T,
                         term_weights.T)).T
              for terms, term_weights
              in zip(sorted_terms, sorted_weights)]

    return topics

