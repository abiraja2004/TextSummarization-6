"""
Text Normalization - process of cleaning, normalizing , and standardizing textual data (remove special symbols and
    characters, HTML tags, stop words, correct spelling, stemming, lemmatization.
"""

import re
import string
import unicodedata
from HTMLParser import HTMLParser
import nltk

html_parser = HTMLParser()
stopword_list = nltk.corpus.stopwords.words('english')


def extract_sentences(document):
    if isinstance(document, list):
        return document
    document = re.sub('\n', ' ', document)
    if isinstance(document, str):
        document = document
    elif isinstance(document, unicode):
        return unicodedata.normalize('NFKD', document).encode('ascii', 'ignore')
    else:
        raise ValueError('Document is not string or unicode!')
    document = document.strip()
    sentences = nltk.sent_tokenize(document)
    sentences = [sentence.strip() for sentence in sentences]
    return sentences


def unescape_html(text):
    text = html_parser.unescape(text)
    return text


def expand_contractions(text):
    from src.util.contractions import CONTRACTION_MAP
    
    contractions_pattern = re.compile('({})'.format('|'.join(CONTRACTION_MAP.keys())), flags=re.IGNORECASE|re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = \
            CONTRACTION_MAP.get(match) if CONTRACTION_MAP.get(match) else CONTRACTION_MAP.get(match.lower())
        expanded_contraction = first_char+expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text


def pos_tag_text(text):
    import pattern.en
    from nltk.corpus import wordnet as wn
    
    def penn_to_wn_tags(pos_tag):
        if pos_tag.startswith('J'):
            return wn.ADJ
        elif pos_tag.startswith('V'):
            return wn.VERB
        elif pos_tag.startswith('N'):
            return wn.NOUN
        elif pos_tag.startswith('R'):
            return wn.ADV
        else:
            return None
    
    tagged_text = pattern.en.tag(text)
    tagged_lower_text = [(word.lower(), penn_to_wn_tags(pos_tag)) for word, pos_tag in tagged_text]
    return tagged_lower_text


def lemmatize_text(text):
    from nltk.stem import WordNetLemmatizer
    wnl = WordNetLemmatizer()
    
    pos_tagged_text = pos_tag_text(text)
    lemmatized_tokens = [wnl.lemmatize(word, pos_tag) if pos_tag else word for word, pos_tag in pos_tagged_text]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text


def tokenize_text(text):
    tokens = nltk.word_tokenize(text) 
    tokens = [token.strip() for token in tokens]
    return tokens


def remove_special_characters(text):
    tokens = tokenize_text(text)
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub(' ', token) for token in tokens])
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


def remove_stopwords(text):


    tokens = tokenize_text(text)
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text


def normalize_document(document, esc_html=True, expand_cont=True, lemmatize=True, tokenize=False,
                       remove_special_char=True, remove_stop_words=True):
    """
    Main function of the text normalization util that allows users to specify document that they want to process along
        with number of action to take, i.e. remove stop words, perform stemming or lemmatization, etc
    """
    sentences = extract_sentences(document)

    normalized_corpus = []  
    for sentence in sentences:
        if esc_html:
            sentence = html_parser.unescape(sentence)

        if expand_cont:
            sentence = expand_contractions(sentence)

        if lemmatize:
            sentence = lemmatize_text(sentence)
        else:
            sentence = sentence.lower()

        if remove_special_char:
            sentence = remove_special_characters(sentence)

        if remove_stop_words:
            sentence = remove_stopwords(sentence)

        if tokenize:
            sentence = tokenize_text(sentence)
            normalized_corpus.append(sentence)
        else:
            normalized_corpus.append(sentence)
            
    return normalized_corpus
