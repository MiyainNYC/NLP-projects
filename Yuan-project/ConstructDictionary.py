from six import iteritems
from gensim import corpora
from nltk.corpus import stopwords
import os
stoplist = stopwords.words('english')


os.chdir("C:\\Users\\Miya\\OneDrive\\Miya'sGithub\\NLP-for-CNY-Trending\\datasets")


dictionary = corpora.Dictionary(line.split() for line in open('lead_paragraph_cleaned.txt'))

stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]

once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]

## remove stopwords and words appearing once

dictionary.filter_tokens(stop_ids + once_ids)

dictionary.compactify() ## remove gaps in id sequence after words

print(dictionary)
