from src.topic_modeling.latent_semantic_indexing import print_topics
from nltk.corpus import gutenberg


toy_corpus = ["The fox jumps over the dog",
              "The fox is very clever and quick",
              "The dog is slow and lazy",
              "The cat is smarter than the fox and the dog",
              "Python is an excellent programming language",
              "Java and Ruby are other programming languages",
              "Python and Java are very popular programming languages",
              "Python programs are smaller than Java programs"]


print_topics(corpus=toy_corpus, total_topics=2, num_terms=5, display_weights=True)

alice = gutenberg.sents(fileids='carroll-alice.txt')
alice = [' '.join(ts) for ts in alice]

print_topics(corpus=alice, total_topics=50, num_terms=50, display_weights=True)
