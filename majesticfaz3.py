import psycopg2
import numpy as np
import pandas as pd
import psycopg2.extras as extras
from tldextract import extract

conn = psycopg2.connect("dbname=postgres user=postgres password=123456")
#yeni majestic csv okunur
df = pd.read_csv('https://downloads.majestic.com/majestic_million.csv')
#dbdeki önceden çekilmiş veriler çekilir
query = "SELECT  * FROM majestic_million"
cursor = conn.cursor()
cursor.execute(query)
for index, row in df.iterrows():
    #yeni csvdeki sütunlar düzenlenip tupleda tutulur
    tsd, td, tsu = extract(row["Domain"])
    liste = (row["GlobalRank"],row["Domain"],row["TLD"],row["TldRank"],td)
    #dbdeki eski veriler tek tek kontrol edilir.
    db_row = cursor.fetchone()
    #farklı olanlar basılır
    if(liste != db_row):
        print(db_row)
    conn.commit()

conn.close()
