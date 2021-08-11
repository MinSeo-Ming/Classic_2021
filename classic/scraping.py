import requests
from bs4 import BeautifulSoup

#수정해야하는 크롤링 코드

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = "https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query="
keyword = input("옷종류")# 종류 별로 넣어두는 것보다 그때 그때 실행하게 하는 게 좋을 ㅓㄱ 같은데... 이럭ㄴ 강사님께 물어봐야지.
url  = url + keyword
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
musicLists = soup.select('#body-content > div.newest-list > div > table > tbody > tr')