"""
Document summarization techniques:
- Extraction-based:  use math and stats like SVD to extract key subset from original. The content can be words, phrases,
                     or sentences. End result is a short summary of a couple of lines that are extracted from the
                     original document. No need content is generated.
                     Latent Semantic Analysis, TextRank
- Abstraction-based: More complex than previous technique. Leverages language semantics to generate text on its own
                     and creates summaries like human would write them.
"""
from text_rank import get_text_summarization_gensim, get_text_summarization_text_rank
from lsa import get_text_summarization_lsa


def get_text_summarization(text, method='text_rank'):
    if method == 'text_rank':
        summary = get_text_summarization_text_rank(text=text)
        return summary
    elif method == 'gensim':
        summary = get_text_summarization_gensim(text=text)
        return summary
    elif method == 'lsa':
        summary = get_text_summarization_lsa(text=text)
        return summary
    else:
        raise Exception("Wrong model type entered. Possible values: 'text_rank', 'lsa', 'gensim")


def print_summary(summary):
    for sentence in summary:
        print sentence
