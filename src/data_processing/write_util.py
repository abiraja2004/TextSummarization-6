def perform_text_processing(raw_text):
    """ Perform key phrase extraction """
    from src.keyphrase_extraction.keyphrase_extraction import get_keyphrases, print_keyphrases

    keyphrase_collocation = get_keyphrases(corpus=raw_text, method='col', number_of_keyphrases=5)
    print "===== Keyphrases extracted via Collocation method ====="
    print_keyphrases(keyphrases=keyphrase_collocation)
    print

    keyphrase_wtp = get_keyphrases(corpus=raw_text, method='wtp', number_of_keyphrases=5)
    print "===== Keyphrases extracted via Weighted Tag-based Phrase extraction method ====="
    print_keyphrases(keyphrases=keyphrase_wtp)

    """ Perform topic modeling """
    from src.topic_modeling.topic_modeling import print_topics, get_topics, topics_map

    num_of_topics = 2

    print "===== Topic Modeling via LDA ====="
    topics_lda = get_topics(corpus=raw_text, model_type='lda', total_topics=num_of_topics)
    topics_lda_map = topics_map(topics_lda, total_topics=num_of_topics)
    print_topics(topic_model=topics_lda, total_topics=num_of_topics, display_weights=True, num_terms=5)

    print "===== Topic Modeling via LSI ====="
    topics_lsi = get_topics(corpus=raw_text, model_type='lsi', total_topics=num_of_topics)
    topics_lsi_map = topics_map(topics_lsi, total_topics=num_of_topics)
    print_topics(topic_model=topics_lsi, total_topics=num_of_topics, display_weights=True, num_terms=5)

    print "===== Topic Modeling via NMF ====="
    topics_nmf = get_topics(corpus=raw_text, model_type='nmf', total_topics=num_of_topics)
    topics_nmf_map = topics_map(topics_nmf, total_topics=num_of_topics)
    print_topics(topic_model=topics_nmf, total_topics=num_of_topics, display_weights=True, num_terms=5)

    """ Perform text summarization """
    from src.document_summarization.document_summarization import get_text_summarization, print_summary

    summary_gensim = get_text_summarization(text=raw_text, method='gensim')
    print "===== Text Summarization via Gensim implementation of TextRank  ====="
    print_summary(summary=summary_gensim)
    print

    summary_lsa = get_text_summarization(text=raw_text, method='lsa')
    print "===== Text Summarization via LSA ====="
    print_summary(summary=summary_lsa)
    print

    summary_tr = get_text_summarization(text=raw_text, method='text_rank')
    print "===== Text Summarization via TextRank ====="
    print_summary(summary=summary_tr)

    return \
        keyphrase_collocation, keyphrase_wtp, topics_lsi_map, topics_lda_map, topics_nmf_map, \
        summary_gensim, summary_lsa, summary_tr


def write_to_excel(file_name, output_data):
    from src.data_processing import extraction_util as eu
    """ Write out the extracted data and results of performed analysis """
    import xlsxwriter
    import datetime

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(
        'data\output\\' + file_name + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.xlsx')

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    """ Raw field of the invention text """
    worksheet_0 = workbook.add_worksheet(eu.FIELD_OF_THE_INVENTION.upper())
    row = 0
    col = 0
    for line in output_data['raw_field_invention']:
        worksheet_0.write(row, col, line)
        row += 1

    """ Raw description of the related art text """
    worksheet_00 = workbook.add_worksheet(eu.DESC_OF_THE_RELATED_ART.upper())
    row = 0
    col = 0
    for line in output_data['raw_rel_art']:
        worksheet_00.write(row, col, line)
        row += 1

    """ Raw summary text """
    worksheet_1 = workbook.add_worksheet(eu.SUMMARY_OF_THE_INVENTION.upper())
    row = 0
    col = 0
    for line in output_data['raw_summary']:
        worksheet_1.write(row, col, line)
        row += 1

    """ Extracted summaries """
    worksheet_2 = workbook.add_worksheet("Summary Topic Summary")
    row = 0
    col = 0
    worksheet_2.write(row, col, "Gensim Summarization", bold)
    for sentence in output_data['summary_summary_gensim']:
        row += 1
        worksheet_2.write(row, col, sentence)

    row += 1
    worksheet_2.write(row, col, "")
    row += 1
    worksheet_2.write(row, col, "LSA Summarization", bold)
    for sentence in output_data['summary_summary_lsa']:
        row += 1
        worksheet_2.write(row, col, sentence)

    row += 1
    worksheet_2.write(row, col, "")
    row += 1
    worksheet_2.write(row, col, "TextRank Summarization", bold)
    for sentence in output_data['summary_summary_tr']:
        row += 1
        worksheet_2.write(row, col, sentence)

    """ Extracted keyphrases """
    worksheet_3 = workbook.add_worksheet("Summary Keyphrases")
    row = 0
    col = 0
    worksheet_3.write(row, col, "Keyphrases extracted via Collocation method", bold)
    for keyphrase in output_data['summary_keyphrase_collocation']:
        row += 1
        worksheet_3.write(row, col, keyphrase[0])

    row += 1
    worksheet_3.write(row, col, "")
    row += 1
    worksheet_3.write(row, col, "Keyphrases extracted via Weighted Tag-based Phrase extraction method", bold)
    for keyphrase in output_data['summary_keyphrase_wtp']:
        row += 1
        worksheet_3.write(row, col, keyphrase[0])

    """ Extracted topics """
    worksheet_4 = workbook.add_worksheet("Summary Topics")
    row = 0
    col = 0
    worksheet_4.write(row, col, "Topic Modeling via LSI", bold)
    for key, value in output_data['summary_topics_lsi_map'].iteritems():
        row += 1
        worksheet_4.write(row, 0, key)
        for val in value:
            row += 1
            worksheet_4.write(row, 1, val)

    row += 1
    worksheet_4.write(row, col, "")
    row += 1
    worksheet_4.write(row, col, "Topic Modeling via LDA", bold)
    for key, value in output_data['summary_topics_lda_map'].iteritems():
        row += 1
        worksheet_4.write(row, 0, key)
        for val in value:
            row += 1
            worksheet_4.write(row, 1, val)

    row += 1
    worksheet_4.write(row, col, "")
    row += 1
    worksheet_4.write(row, col, "Topic Modeling via NMF", bold)
    for key, value in output_data['summary_topics_nmf_map'].iteritems():
        row += 1
        worksheet_4.write(row, 0, key)
        for val in value:
            row += 1
            worksheet_4.write(row, 1, val)

    """ Raw desc text """
    worksheet_5 = workbook.add_worksheet("description of the invention".upper())
    row = 0
    col = 0
    for line in output_data['raw_desc']:
        worksheet_5.write(row, col, line)
        row += 1

    """ Extracted summaries """
    worksheet_6 = workbook.add_worksheet("Invention Topic Summary")
    row = 0
    col = 0
    worksheet_6.write(row, col, "Gensim Summarization", bold)
    for sentence in output_data['desc_summary_gensim']:
        row += 1
        worksheet_6.write(row, col, sentence)

    row += 1
    worksheet_6.write(row, col, "")
    row += 1
    worksheet_6.write(row, col, "LSA Summarization", bold)
    for sentence in output_data['desc_summary_lsa']:
        row += 1
        worksheet_6.write(row, col, sentence)

    row += 1
    worksheet_6.write(row, col, "")
    row += 1
    worksheet_6.write(row, col, "TextRank Summarization", bold)
    for sentence in output_data['desc_summary_tr']:
        row += 1
        worksheet_6.write(row, col, sentence)

    """ Extracted keyphrases """
    worksheet_7 = workbook.add_worksheet("Invention Keyphrases")
    row = 0
    col = 0
    worksheet_7.write(row, col, "Keyphrases extracted via Collocation method", bold)
    for keyphrase in output_data['desc_keyphrase_collocation']:
        row += 1
        worksheet_7.write(row, col, keyphrase[0])

    row += 1
    worksheet_7.write(row, col, "")
    row += 1
    worksheet_7.write(row, col, "Keyphrases extracted via Weighted Tag-based Phrase extraction method", bold)
    for keyphrase in output_data['desc_keyphrase_wtp']:
        row += 1
        worksheet_7.write(row, col, keyphrase[0])

    """ Extracted topics """
    worksheet_8 = workbook.add_worksheet("Invention Topics")
    row = 0
    col = 0
    worksheet_8.write(row, col, "Topic Modeling via LSI", bold)
    for key, value in output_data['desc_topics_lsi_map'].iteritems():
        row += 1
        worksheet_8.write(row, 0, key)
        for val in value:
            row += 1
            worksheet_8.write(row, 1, val)

    row += 1
    worksheet_8.write(row, col, "")
    row += 1
    worksheet_8.write(row, col, "Topic Modeling via LDA", bold)
    for key, value in output_data['desc_topics_lda_map'].iteritems():
        row += 1
        worksheet_8.write(row, 0, key)
        for val in value:
            row += 1
            worksheet_8.write(row, 1, val)

    row += 1
    worksheet_8.write(row, col, "")
    row += 1
    worksheet_8.write(row, col, "Topic Modeling via NMF", bold)
    for key, value in output_data['desc_topics_nmf_map'].iteritems():
        row += 1
        worksheet_8.write(row, 0, key)
        for val in value:
            row += 1
            worksheet_8.write(row, 1, val)


    workbook.close()
