from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


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