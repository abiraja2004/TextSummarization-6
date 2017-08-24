"""
Feature Extraction - extract meaningful features. Also known as vectorization, so that algorithms can work on
    numerical vectors.
Feature Matrix - mapping from a collection of documents to features where each row indicates documents and each
    column indicates a particular feature.
"""
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.sparse.linalg import svds


def build_feature_matrix(documents, feature_type='frequency'):

    feature_type = feature_type.lower().strip()  
    
    if feature_type == 'binary':
        # Binary term occurrence-based features
        vectorizer = CountVectorizer(binary=True, min_df=1, ngram_range=(1, 1))
    elif feature_type == 'frequency':
        # Frequency bag of words-based features
        vectorizer = CountVectorizer(binary=False, min_df=1, ngram_range=(1, 1))
    elif feature_type == 'tfidf':
        # TF-IDF-weighted features
        vectorizer = TfidfVectorizer(min_df=1, ngram_range=(1, 1))
    else:
        raise Exception("Wrong feature type entered. Possible values: 'binary', 'frequency', 'tfidf'")

    feature_matrix = vectorizer.fit_transform(documents).astype(float)
    
    return vectorizer, feature_matrix


def low_rank_svd(matrix, singular_count=2):
    u, s, vt = svds(matrix, k=singular_count)
    return u, s, vt
