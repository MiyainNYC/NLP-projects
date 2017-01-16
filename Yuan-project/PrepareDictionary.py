import glob
import pandas as pd

import os
import timeit
import string

start = timeit.timeit()

os.chdir("C:\\Users\\Miya\\OneDrive\\Miya'sGithub\\NLP-for-CNY-Trending\\datasets")

df_all = pd.DataFrame()
for i in glob.glob('*[0-9].csv'):
    df = pd.read_csv(i)
    df_all = pd.concat([df,df_all],ignore_index=True)


df_all['date'] = pd.to_datetime(df_all['date'])
df_all['YearMonth'] = df_all['date'].map(lambda x: str(x.year) + '-'+str(x.month))
df_all['YearMonth']  = pd.to_datetime(df_all['YearMonth'])

n=0
lead_paragraph = []
for i in df_all['lead_paragraph'].isnull():
    if i==False:
        lead_paragraph.append(df_all['lead_paragraph'].values[n])
    else:
        lead_paragraph.append(df_all['headline'].values[n])
    n = n+1


df_all['lead_paragraph'] = lead_paragraph

lead_paragraph_cleaned = [i.translate(None, string.punctuation).translate(None, string.digits) for i in lead_paragraph]

thedictionary = open('lead_paragraph_cleaned.txt', 'w')
for item in lead_paragraph_cleaned:
    thedictionary.write("%s\n" % item)

end = timeit.timeit()

print('lead paragraph cleaned saved!')

print end - start
