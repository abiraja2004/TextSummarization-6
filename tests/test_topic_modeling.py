from src.topic_modeling.topic_modeling import print_topics


toy_corpus = ["The fox jumps over the dog",
              "The fox is very clever and quick",
              "The dog is slow and lazy",
              "The cat is smarter than the fox and the dog",
              "Python is an excellent programming language",
              "Java and Ruby are other programming languages",
              "Python and Java are very popular programming languages",
              "Python programs are smaller than Java programs"]


print_topics(corpus=toy_corpus, model_type='lsi', total_topics=2, num_terms=5, display_weights=True)

print_topics(corpus=toy_corpus, model_type='lda', total_topics=2, num_terms=5, display_weights=True)

print_topics(corpus=toy_corpus, model_type='nmf', total_topics=2, num_terms=None, display_weights=True)
