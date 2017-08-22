#import nltk
#nltk.download()

from nltk.corpus import gutenberg
from text_normalization_util import normalize_document
from keyphrase_extraction_util import retrieve_top_ngrams_collocations, retrieve_top_bigrams_collocations, \
    retrieve_top_trigrams_collocations, retrieve_weighted_tagbased_phrase

alice = gutenberg.sents(fileids='carroll-alice.txt')
alice = [' '.join(ts) for ts in alice]

norm_alice = filter(None, normalize_document(alice, lemmatize=False))

# print "\n$ Raw text"
# print alice[0]
# print alice[1]
# print alice[2]
# print alice[3]
#
# print "\n$ Normalized text"
# print norm_alice[0]
# print norm_alice[1]
# print norm_alice[2]
# print norm_alice[3]
#
# result = retrieve_top_ngrams_collocations(corpus=norm_alice, ngram_size=2, top=10)
# print "\n$ Print top 10 bigrams (manually)"
# print result
#
# # find raw frequencies of bigrams
# result = retrieve_top_bigrams_collocations(corpus=norm_alice, top=10, measure='frequency')
# print "\n$ Print top 10 bigrams (raw frequences)"
# print result
#
# # find pointwise mutual information of bigrams
# result = retrieve_top_bigrams_collocations(corpus=norm_alice, top=10, measure='pmi')
# print "\n$ Print top 10 bigrams (pointwise mutal information)"
# print result
#
# # find raw frequencies of trigrams
# result = retrieve_top_trigrams_collocations(corpus=norm_alice, top=10, measure='frequency')
# print "\n$ Print top 10 trigrams (raw frequences)"
# print result
#
# # find pointwise mutual information of trigrams
# result = retrieve_top_trigrams_collocations(corpus=norm_alice, top=10, measure='pmi')
# print "\n$ Print top 10 trigrams (pointwise mutal information)"
# print result

toy_text = """
Elephants are large mammals of the family Elephantidae
and the order Proboscidea. Two species are traditionally recognised,
the African elephant and the Asian elephant. Elephants are scattered
throughout sub-Saharan Africa, South Asia, and Southeast Asia. Male
African elephants are the largest extant terrestrial animals. All
elephants have a long trunk used for many purposes,
particularly breathing, lifting water and grasping objects. Their
incisors grow into tusks, which can serve as weapons and as tools
for moving objects and digging. Elephants' large ear flaps help
to control their body temperature. Their pillar-like legs can
carry their great weight. African elephants have larger ears
and concave backs while Asian elephants have smaller ears
and convex or level backs.
"""

result = retrieve_weighted_tagbased_phrase(corpus=alice, top=50)
print result
