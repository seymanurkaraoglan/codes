import redis
import pandas as pd
from tldextract import extract
 
df = pd.read_csv('https://downloads.majestic.com/majestic_million.csv')

# Create a redis client

redisClient = redis.StrictRedis(host='localhost',

                                port=6379,

                                db=0)

for index,row in df.iterrows():
    tsd, td, tsu = extract(row["Domain"])
    redisClient.hset('MajesticMillionn',td,1)