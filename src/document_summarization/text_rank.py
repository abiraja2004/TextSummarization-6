"""
TextRank Algorithm summary:
    1. Tokenize and extract sentences from the document
    2. Determine number of sentences that we want in final summary
    3. Build document term feature matrix using weights like TF-IDF or Bag-of-Words
    4. Compute a document similarity matrix by multiplying the matrix with its transpose
    5. Use these documents as the vertices and the similarities between each pair of documents as the weight or score
       coefficient and feed them to the PageRank algorithm.
    6. Get the score for each sentence
    7. Rank the sentences based on the score and return top N sentences
"""
from gensim.summarization import summarize
from src.util.text_normalization_util import extract_sentences, normalize_document
from src.util.feature_extraction_util import build_feature_matrix
import networkx


def get_text_summarization_gensim(text, summary_ratio=0.4):
    """
    summary_ratio should be a number between 0 and 1 that determines the percentage of the number of sentences of the
        original text to be chosen for the summary
    """
    sentences = extract_sentences(text)
    text = ' '.join(sentences)
    summary = summarize(text, split=True, ratio=summary_ratio)
    return summary


def get_text_summarization_text_rank(text, num_sentences=3, feature_type='tfidf'):
    # parse and normalize document
    normalized_sentences = normalize_document(text, lemmatize=False, expand_cont=False, remove_special_char=False,
                                              remove_stop_words=False, lower_case=False)
    # construct weighted document term matrix
    vec, dt_matrix = build_feature_matrix(normalized_sentences, feature_type=feature_type)
    # construct the document similarity matrix
    similarity_matrix = (dt_matrix * dt_matrix.T)
    # build the similarity graph
    similarity_graph = networkx.from_scipy_sparse_matrix(similarity_matrix)
    # compute pagerank scores for all the sentences
    scores = networkx.pagerank(similarity_graph)
    # rank sentences based on their scores
    ranked_sentences = sorted(((score, index) for index, score in scores.items()), reverse=True)
    # get the top sentence indices for our summary
    top_sentence_indices = [ranked_sentences[index][1] for index in range(num_sentences)]
    top_sentence_indices.sort()
    # construct the document summary
    summary_sentences = []
    for index in top_sentence_indices:
        summary_sentences.append(normalized_sentences[index])

    return summary_sentences
