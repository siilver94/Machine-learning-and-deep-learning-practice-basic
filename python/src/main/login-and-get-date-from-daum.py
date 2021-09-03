import requests
from bs4 import BeautifulSoup

#세션 만들기
session = requests.session()

#로그인
url = 'https://logins.daum.net/accounts/srp.do?slevel=1&rid=a820fe91-e068-468e-bc94-cdfc9759ed47&srplm1=2e4d43b2fa0a02abbd540bf4993d5e8a2d2932b76fca821f3d77e5f8651747a2'
data = {'url': 'https://www.daum.net/',
        'id': 'silver_94',
        'pw': 'hackzld2035',
        }

response = session.post(url, data=data)
response.raise_for_status()

#메일 정보 들고오기
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
url = 'https://www.daum.net/'
response = session.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
text = soup.find('strong', attrs = {'class':'date_today'}).get_text()

print('오늘의 날짜 : ', text)
