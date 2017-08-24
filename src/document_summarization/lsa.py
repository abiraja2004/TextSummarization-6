"""
Latent Semantic Analysis
There exists a latent structure among terms, which are related contextually and hence should also be correlated in the
same singular space.
"""
from src.util.feature_extraction_util import build_feature_matrix, low_rank_svd
from src.util.text_normalization_util import extract_sentences
import numpy as np


def get_text_summarization_lsa(text, num_sentences=3, num_topics=3, feature_type='frequency', sv_threshold=0.5):
    sentences = extract_sentences(text)
    vec, dt_matrix = build_feature_matrix(sentences, feature_type=feature_type)

    td_matrix = dt_matrix.transpose()
    td_matrix = td_matrix.multiply(td_matrix > 0)

    u, s, vt = low_rank_svd(td_matrix, singular_count=num_topics)
    min_sigma_value = max(s) * sv_threshold
    s[s < min_sigma_value] = 0

    salience_scores = np.sqrt(np.dot(np.square(s), np.square(vt)))
    top_sentence_indices = salience_scores.argsort()[-num_sentences:][::-1]
    top_sentence_indices.sort()

    summary_sentences = []
    for index in top_sentence_indices:
        summary_sentences.append(sentences[index])

    return summary_sentences
