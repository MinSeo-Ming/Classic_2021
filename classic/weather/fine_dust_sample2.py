import urllib.parse
import requests
import xml.etree.cElementTree as ET


skey = "fZGJv4qdHkRkYM1q%2FbbjbHYf5HJYQRepSohikfUPTb1cZlFEdir59IHXG7ATlm2jhlaicmV5uLlu8uhIRbf3Fg%3D%3D"
decoded_key = urllib.parse.unquote(skey)
# print(decoded_key)

url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth"
params = {
    "Servicekey": decoded_key,
    "pageNo" : "10",
    "numOfRows": "10",
    "searchDate": "2021-08-03",
    "returnType": "xml",
    "InformCode": "PM10"

}

resp = requests.get(url, params=params)
root = ET.fromstring(resp.content)

items = []
for element in root.iter('item'):
    item = {}
    item['informCode'] = element.find('informCode').text
    item['informData'] = element.find('informData').text
    item['informGrade'] = element.find('informGrade').text
    item['informCause'] = element.find('informCause').text
    items.append(item)
 

for item in items :
        print(item)

# 미세먼지 기준
# PM 0~30: 좋음, 31~80:보통, 81~150:나쁨, 151이상: 매우나쁨