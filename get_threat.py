import json
import sys
#request gönderdikten sonra urlden dene
f= open("C://Users//eynan//OneDrive//Masaüstü//response.json")
parsed = json.load(f)
data = json.dumps(parsed,indent=4)
#items["threat_level_human"] == "suspicious"
infos = []
for items in parsed["data"]:
   if(items["threat_level_human"] == "malicious" or items["threat_level_human"] == "suspicious"):
        for k,v in items.items():
            if(k == "vx_family" and v == "Malware site"):

                s = ','.join(items["hosts"])
                infos.append(items['submit_name'])
                infos.append(s)
                infos.append(items["md5"])
                infos.append(items["sha1"])
                infos.append(items["sha256"])
