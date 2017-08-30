# Text Summarization

1.	Used https://bulkdata.uspto.gov/ to download some sample data. More specifically: https://bulkdata.uspto.gov/data/patent/application/redbook/2017/I20170105.tar 
2.	Analyzed downloaded XML (https://prod-cicm.uspto.gov/gitlab/ekrinker/TextSummarization/blob/master/data/input/US20170000001A1-20170105.XML) and noticed that it contained four sections of interest, more specifically
..*Field of the Invention
..*Description of the Related Art
..*SUMMARY OF THE INVENTION
..*DETAILED DESCRIPTION OF THE INVENTION
(Other downloaded files that I looked at had similar XML structure)
3.	I wrote xml parser to be able to extract the data out of the XML and make it available for further processing
4.	I added following ML modules
o	Key Phrase Extraction – The idea here is to identify key phrases that might help examiners to better form their search queries.
	via Collocation
	via Weighted Tag based Phrase Extraction
o	Topic Modeling – This one is experimental on how to can use it, if we can. Still playing with it (defaults to 2 topics for now, but configurable).
	via Latent Semantic Indexing
	via Latent Dirichlet Allocation
	via Nonnegative Matrix Factorization
o	Document Summarization – the algorithms that I used are ‘extraction based’, i.e. they will try to identify important sentences and would extract them to form a summary from original. No new content will be generated (unlike when summary is written by humans)
	via Text Rank
	via Latent Semantic Analysis
	via Gensim (python library) summarization function which is built on top of Text Rank
5.	Ran extracted ‘SUMMARY OF THE INVENTION’ and ‘DETAILED DESCRIPTION OF THE INVENTION’ from step 3 through the algorithms in step 4.
6.	Generated excel spreadsheet (attached) to list extracted raw text from step 3, and results of step 5 in different tabs.
