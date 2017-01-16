import pandas as pd
import sqlite3
import os
from sqlite3 import OperationalError

os.chdir("C:\\Users\\Miya\\OneDrive\\Miya'sGithub\\NLP-for-CNY-Trending\\datasets")


def db_create():
    df_all = pd.read_csv('df-all.csv', encoding='iso-8859-1')
    del df_all['Unnamed: 0']
    conn = sqlite3.connect("NYTimes.db")

    cur = conn.cursor()

    init_query = "create table NYTIMES" + '(' + ",".join(df_all.columns) + ')'
    try:
        cur.execute(init_query)
    except OperationalError:
        print("database already there!")

    execute_query = ("INSERT INTO NYTIMES" + ' (' + ",".join(df_all.columns) + ')' +
                     ' values ' + '(' + '?,' * (len(df_all.columns) - 1) + '?' + ')')

    for i in df_all.values:
        cur.execute(execute_query, tuple(i))

    cur.execute('select * from NYTIMES')

    all_contents = cur.fetchall()

    if len(all_contents) == len(df_all):
        print("everything is right")
    else:
        print("something is wrong!")