# Text Summarization

1.	Use https://bulkdata.uspto.gov/ to download data. For example: https://bulkdata.uspto.gov/data/patent/application/redbook/2017/I20170105.tar 
2.	Each file (for example https://prod-cicm.uspto.gov/gitlab/ekrinker/TextSummarization/blob/master/data/input/US20170000001A1-20170105.XML) would contain following four sections:
  * Field of the Invention.
  * Description of the Related Art.
  * SUMMARY OF THE INVENTION.
  * DETAILED DESCRIPTION OF THE INVENTION.
3.	XML parser (src/data_processing/extraction_util.py) will be able to extract the data out of the XML and make it available for further processing.
4.	Following ML modules are run on the extracted corpus:
  * Key Phrase Extraction – The idea here is to identify key phrases that might help examiners to better form their search queries.
    - via Collocation.
    - via Weighted Tag based Phrase Extraction.
  * Topic Modeling – Allows examiner to identify topics contained in the corpus.
    - via Latent Semantic Indexing.
    - via Latent Dirichlet Allocation.
    - via Nonnegative Matrix Factorization.
  * Document Summarization – the algorithms that were used are ‘extraction based’, i.e. they will try to identify important sentences and would extract them to form a summary from original. No new content will be generated (unlike when summary is written by humans).
    - via Text Rank.
    - via Latent Semantic Analysis.
    - via Gensim (python library) summarization function which is built on top of Text Rank.
5.	Extracted ‘SUMMARY OF THE INVENTION’ and ‘DETAILED DESCRIPTION OF THE INVENTION’ sections from step 3 will be run through the algorithms in step 4.
6.	The program would generate excel spreadsheet to list extracted raw text from step 3, and results of step 5 in different tabs. 
  * See 'sample' for example of input and output.
