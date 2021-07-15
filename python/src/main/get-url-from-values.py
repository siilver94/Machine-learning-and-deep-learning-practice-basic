import urllib.request
import urllib.parse

api = 'https://search.naver.com/search.naver'
values = {
    'where': 'nexearch',
    'sm': 'top_hty',
    'fbm': '1',
    'ie': 'utf8',
    'query': '초콜릿'
}

params = urllib.parse.urlencode(values)
url = api+'?'+params

print(url)
