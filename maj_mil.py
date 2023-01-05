import psycopg2
import numpy as np
import psycopg2.extras as extras
import pandas as pd
from urllib.parse import urlparse
from tldextract import extract

class majestic_million:
    def insert_to_table(self):
        #Önce db bağlantısı gerçekleştirilir
        conn = psycopg2.connect("dbname=postgres user=postgres password=123456")
        # pandas ile csv linki okunur
        df = pd.read_csv('https://downloads.majestic.com/majestic_million.csv')
        #insert edelim
        for index, row in df.iterrows():
            tsd, td, tsu = extract(row["Domain"])
            query = "INSERT INTO majestic_millionn(rank,hostname,domain,tldrank,tld) VALUES (%s,%s,%s,%s,%s)" 
            cursor = conn.cursor()
            liste = (row["GlobalRank"],td,row["Domain"],row["TldRank"],row["TLD"])
            try:
                cursor.execute(query,liste)
                # herhangi bir hata varsa bastırılır,hata çıkarsa işlemler başa döner.Bağlantı kapatılır
            except (Exception, psycopg2.DatabaseError) as error:
                    print("Error: %s" % error)
                    conn.rollback()
                    cursor.close()
        conn.commit()
        print("the dataframe is inserted")
        cursor.close()

mm = majestic_million()
mm.insert_to_table()