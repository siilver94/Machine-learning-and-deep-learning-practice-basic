import urllib.request 

url ='http://uta.pw/shodou/img/28/214.png'
savename = 'test.png'

mem = urllib.request.urlopen(url).read()

with open (savename, mode='wb') as f:
    f.write(mem)
    print('저장되었습니다')

    
# 도커에서, ls -l명령어를 통해 파이썬 파일이 있는 것을 확인하고
# 도커 내에서 파이썬 명령어를 통해서 코드를 실행시키면
# 코드에서 처럼 파일을 다운로드 하고
# 다시 ls -l상태명령어를 통해 새로운 png파일이 생긴것을 확인 가능
