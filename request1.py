from traceback import print_tb
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/106.0.0.0 Safari/537.36',
           'api-key' : 'hw7c1g2a1747355e9pk1imvk70a8b969lbt24dyi5f17c362ta8sscmg745ea1fa'}

"""url = "https://www.hybrid-analysis.com/api/v2/quick-scan/state"
r = requests.get(url,headers=headers)
print(r.text)
"""


"""p= {'scan_type':'all','url':'https://www.hybrid-analysis.com/submissions/sandbox/urls?sort=timestamp&sort_order=desc&page=1'}
url = "https://www.hybrid-analysis.com/api/v2/quick-scan/url"
r = requests.post(url,headers=headers,data=p)
print(r.text)
"""
"""url = "https://www.hybrid-analysis.com/api/v2/submit/url"
p={'environment_id': '300','url':'https://www.hybrid-analysis.com/submissions/sandbox/urls?sort=timestamp&sort_order=desc&page=1'}
r = requests.post(url,headers=headers,data=p)
print(r.text)
"""
from bs4 import BeautifulSoup
import json
import os
"""
#son atılan istekleri döndürür
url = "https://www.hybrid-analysis.com/api/v2/feed/latest"
r = requests.get(url,headers=headers)
file = r.text
print(file)

bu şekilde çıktılar verir
print(type(r))
"""
"""
data = {"name":"en-US.4","file_path":"%LOCALAPPDATA%\\Microsoft\\Internet Explorer\\DomainSuggestions\\en-US.4",
"file_size":18176,"sha1":"3c96c993500690d1a77873cd62bc639b3a10653f",
"sha256":"c6a5377cbc07eece33790cfc70572e12c7a48ad8296be25c0cc805a1f384dbad",
"md5":"5a34cb996293fde2cb7a4ac89587393a","description":"Unknown","runtime_process":"iexplore.exe (PID: 3920)",
"threat_level":0,"threat_level_readable":"no specific threat","file_available_to_download":"false"}


"""
#kota ve mevcut kullanım hakkında bilgi döndürür.
url1 = "https://www.hybrid-analysis.com/api/v2/key/submission-quota"
r = requests.get(url1,headers=headers)
print(r.text)

#kullanılan api hakkında bilgi döndürür
url2 = "https://www.hybrid-analysis.com/api/v2/key/current"
r = requests.get(url2,headers=headers)
#print(r.text)
""" mesela bunun outputu
{"api_key":"hw7c1g2a1747355e9pk1imvk70a8b969lbt24dyi5f17c362ta8sscmg745ea1fa",
"auth_level":1,"auth_level_name":"restricted",
"user":{"id":"6349634501aacf24f27c2aed","email":"doyadoyasoya@gmail.com","name":"denemedeneme"}}
"""
#toplam gönderim sayısını döndürür
url3 = "https://www.hybrid-analysis.com/api/v2/system/total-submissions"
r = requests.get(url3,headers=headers)
#print(r.text)

#toplam gönderim sayısı,unique gönderimler,izma kimliği dağılımı,kullanıcı yorumları gibi istatistikleri içerir.
url4 = "https://www.hybrid-analysis.com/api/v2/system/stats"
r = requests.get(url4,headers=headers)
#print(r.text)