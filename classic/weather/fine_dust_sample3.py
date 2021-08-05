import requests, xmltodict 
import json

key= "fZGJv4qdHkRkYM1q%2FbbjbHYf5HJYQRepSohikfUPTb1cZlFEdir59IHXG7ATlm2jhlaicmV5uLlu8uhIRbf3Fg%3D%3D"
url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth?searchDate=2021-08-04&returnType=xml&serviceKey=fZGJv4qdHkRkYM1q%2FbbjbHYf5HJYQRepSohikfUPTb1cZlFEdir59IHXG7ATlm2jhlaicmV5uLlu8uhIRbf3Fg%3D%3D&numOfRows=10&pageNo=1".format(key)

xml = requests.get(url).content
# print(content)
dict = xmltodict.parse(xml)
jsonString = json.dumps((dict['response']['body']),ensure_ascii=False)
jsonObj= json.loads(jsonString)
for item in jsonObj['items']['item']:
    print(item)



