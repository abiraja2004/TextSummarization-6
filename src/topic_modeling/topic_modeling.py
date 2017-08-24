from latent_semantic_indexing import train_lsi_model
from latent_dirichlet_allocation import train_lda_model
from nonnegative_matrix_factorization import train_nmf_model, get_topics_terms_weights


# Generate topics
def get_topics(corpus, model_type='lsi', total_topics=1):
    if model_type == 'lsi':
        # Extract models with Latent Semantic Indexing
        topic_model = train_lsi_model(corpus, total_topics)
        return topic_model
    elif model_type == 'lda':
        # Extract models with Latent Semantic Indexing
        topic_model = train_lda_model(corpus, total_topics)
        return topic_model
    elif model_type == 'nmf':
        # Extract models with Latent Semantic Indexing
        topic_model, vectorizer = train_nmf_model(corpus, total_topics)
        topic_list = get_topics_terms_weights(nmf=topic_model, vectorizer=vectorizer)
        return topic_list
    else:
        raise Exception("Wrong model type entered. Possible values: 'lsi', 'lda', 'nmf'")


# Display the generated topics
def print_topics(topic_model, total_topics=1, weight_threshold=0.0001, display_weights=False, num_terms=None):
    if isinstance(topic_model, list):
        print_topics_from_list(topic_list=topic_model, total_topics=total_topics, weight_threshold=weight_threshold,
                               display_weights=display_weights, num_terms=num_terms)
    else:
        print_topics_from_model(topic_model=topic_model, total_topics=total_topics, weight_threshold=weight_threshold,
                                display_weights=display_weights, num_terms=num_terms)


def print_topics_from_model(topic_model, total_topics, weight_threshold, display_weights, num_terms):
    for index in range(total_topics):
        topic = topic_model.show_topic(index)
        topic = [(word, round(wt, 2)) for word, wt in topic if abs(wt) >= weight_threshold]

        print_topic(topic=topic, display_weights=display_weights, index=index, num_terms=num_terms)


def print_topics_from_list(topic_list, total_topics, weight_threshold, display_weights, num_terms):
    for index in range(total_topics):
        topic = topic_list[index]
        topic = [(term, float(wt)) for term, wt in topic]
        topic = [(word, round(wt, 2)) for word, wt in topic if abs(wt) >= weight_threshold]

        print_topic(topic=topic, display_weights=display_weights, index=index, num_terms=num_terms)


def print_topic(topic, display_weights, index, num_terms):
    if display_weights:
        print 'Topic #' + str(index + 1) + ' with weights'
        print topic[:num_terms] if num_terms else topic
    else:
        print 'Topic #' + str(index + 1) + ' without weights'
        tw = [term for term, wt in topic]
        print tw[:num_terms] if num_terms else tw
    print
