""" Process specified patent xml document and provides key terms, topic modeling and summarization """

""" Load XML file to process and Extract required data """
import ntpath
import os
from src.data_processing import extraction_util as eu
from src.data_processing import write_util as wu

input_file = 'data\input\US20170000002A1-20170105.XML'
extracton_results = eu.extract_application_data(input_file)
file_name = ntpath.basename(os.path.splitext("data\input\US20170000002A1-20170105.XML")[0])

""" Print raw data """
raw_field_invention = extracton_results[eu.FIELD_OF_THE_INVENTION]
print raw_field_invention
raw_rel_art = extracton_results[eu.DESC_OF_THE_RELATED_ART]
print raw_rel_art
raw_summary = extracton_results[eu.SUMMARY_OF_THE_INVENTION]
print raw_summary
raw_desc = extracton_results[eu.DETAILED_DESC_OF_THE_INVENTION]
print raw_desc

summary_keyphrase_collocation, summary_keyphrase_wtp, summary_topics_lsi_map, summary_topics_lda_map, \
    summary_topics_nmf_map, summary_summary_gensim, summary_summary_lsa, summary_summary_tr \
    = wu.perform_text_processing(raw_summary)

desc_keyphrase_collocation, desc_keyphrase_wtp, desc_topics_lsi_map, desc_topics_lda_map, \
    desc_topics_nmf_map, desc_summary_gensim, desc_summary_lsa, desc_summary_tr \
    = wu.perform_text_processing(raw_desc)

output_data = {}
output_data.update({'raw_field_invention': raw_field_invention})
output_data.update({'raw_rel_art': raw_rel_art})

output_data.update({'raw_summary': raw_summary})
output_data.update({'summary_keyphrase_collocation': summary_keyphrase_collocation})
output_data.update({'summary_keyphrase_wtp': summary_keyphrase_wtp})
output_data.update({'summary_topics_lsi_map': summary_topics_lsi_map})
output_data.update({'summary_topics_lda_map': summary_topics_lda_map})
output_data.update({'summary_topics_nmf_map': summary_topics_nmf_map})
output_data.update({'summary_summary_gensim': summary_summary_gensim})
output_data.update({'summary_summary_lsa': summary_summary_lsa})
output_data.update({'summary_summary_tr': summary_summary_tr})

output_data.update({'raw_desc': raw_desc})
output_data.update({'desc_keyphrase_collocation': desc_keyphrase_collocation})
output_data.update({'desc_keyphrase_wtp': desc_keyphrase_wtp})
output_data.update({'desc_topics_lsi_map': desc_topics_lsi_map})
output_data.update({'desc_topics_lda_map': desc_topics_lda_map})
output_data.update({'desc_topics_nmf_map': desc_topics_nmf_map})
output_data.update({'desc_summary_gensim': desc_summary_gensim})
output_data.update({'desc_summary_lsa': desc_summary_lsa})
output_data.update({'desc_summary_tr': desc_summary_tr})

wu.write_to_excel(file_name=file_name, output_data=output_data)



