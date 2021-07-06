import urllib.request 

url ='http://uta.pw/shodou/img/28/214.png'
savename = 'test.png'

# urlretrieve 는 파일을 다운받을 수 있음
urllib.request.urlretrieve(url, savename)  #(어떤 url에 있는것을, 어디에 저장할것인가)
