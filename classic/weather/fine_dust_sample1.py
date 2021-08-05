from bs4 import BeautifulSoup as bs
import requests



html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser') 
#파싱을 통해 html 요소에 접근

data1 = soup.find('div',{'class':'detail_box'})
#매칭되는 처음 1개만 반환

data2 = data1.findAll('dd')
#매칭되는 모든 요소 반환-0:미세먼지, 1:초미세먼지, 2: 오존지수

fine_dust = data2[0].find('span',{'class':'num'}).text
print(fine_dust)
#미세먼지

ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
print(ultra_fine_dust)
#초미세먼지

# 미세먼지 기준
# PM 0~30: 좋음, 31~80:보통, 81~150:나쁨, 151이상: 매우나쁨


