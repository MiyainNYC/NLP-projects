import pandas as pd
import glob
from bs4 import BeautifulSoup
import time
import http.cookiejar, urllib.request
import os

os.chdir("C:\\Users\\Miya\\OneDrive\\Miya'sGithub\\NLP-for-CNY-Trending\\datasets")


cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
def crawl_articles():
    df_all = pd.DataFrame()
    for i in glob.glob('*[0-9].csv'):
        df = pd.read_csv(i)
        df_all = pd.concat([df, df_all], ignore_index=True)

    print(len(df_all))

    df_all['date'] = pd.to_datetime(df_all['date'])
    df_all['YearMonth'] = df_all['date'].map(lambda x: str(x.year) + '-' + str(x.month))
    df_all['YearMonth'] = pd.to_datetime(df_all['YearMonth'])

    url_list = df_all['url']

    start_time = time.clock()
    whole_article = []
    for url in url_list:
        r = opener.open(url_list[0])
        soup = BeautifulSoup(r)
        article = soup.findAll('p', "story-body-text story-content")
        list_a = [i.text for i in article]
        whole_article += ['\n'.join(list_a)]
    time.clock() - start_time

    df_all['whole_article'] = whole_article

    df_all.to_csv('df-all.csv')

    print("Done!")