from src.topic_modeling.topic_modeling import print_topics, get_topics


toy_corpus = ["The fox jumps over the dog",
              "The fox is very clever and quick",
              "The dog is slow and lazy",
              "The cat is smarter than the fox and the dog",
              "Python is an excellent programming language",
              "Java and Ruby are other programming languages",
              "Python and Java are very popular programming languages",
              "Python programs are smaller than Java programs"]

num_of_topics = 2

print "===== Topic Modeling via LDA ====="
topics_lda = get_topics(corpus=toy_corpus, model_type='lda', total_topics=num_of_topics)
print_topics(topic_model=topics_lda, total_topics=num_of_topics, display_weights=True, num_terms=5)

print "===== Topic Modeling via LSI ====="
topics_lsi = get_topics(corpus=toy_corpus, model_type='lsi', total_topics=num_of_topics)
print_topics(topic_model=topics_lsi, total_topics=num_of_topics, display_weights=True, num_terms=5)

print "===== Topic Modeling via NMF ====="
topics_nmf = get_topics(corpus=toy_corpus, model_type='nmf', total_topics=num_of_topics)
print_topics(topic_model=topics_nmf, total_topics=num_of_topics, display_weights=True, num_terms=5)

