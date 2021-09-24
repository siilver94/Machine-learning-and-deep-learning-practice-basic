## PhantomJS + Selenium.
![image](https://user-images.githubusercontent.com/57824945/132130886-8a38772a-b291-49c0-a574-b81c1423605b.png)

<br/>

### PhantomJS란?

헤드리스 브라우저로 요즘 유명한 브라우저.

<br/>

### Headless browser란?

헤드리스 브라우저는 그래픽 유저 인터페이스가 없는 웹브라우저를 뜻합니다. 헤드리스 브라우저는 웹 브라우저와 유사한 환경을 가졌지만 커맨드 라인 인터페이스를 통해 실행하고 제어할 수 있는 브라우저들을 말합니다. 헤드리스 브라우저엔 자바로 작성된 HtmlUnit이라는 것도 많이 사용됐었습니다.

<br/>

### 도커 환경에서 개발환경 설정

<br/>

1. cmd 에서 `docker pull ubuntu:16.04` [우분투 파일 들고오기]
2. `docker run -it ubuntu:16.04` [우분투 실행]
3. `apt-get update` [우분투 업데이트 실시]
4. `apt-get install -y python3 python3-pip`  [y 옵션으로 python3와 python3 pip 설치]
5. `pip3 install selenium`  [셀리니움 설치]
6. `pip3 install beautifulsoup4` [뷰티풀 습 다운]

---

#### 팬텀JS 다운로드

8. `apt-get install -y wget libfontconfig` [펜텀js 다운로드]
9. `mkdir -p /home/root/src && cd$_`  [해당 폴더를 생성]
10. `wget [https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2)` .
    [팬텀js 가져오기]

1. `tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2` [가져온 phantomjs 압축 해체]
2. `cd phantomjs-2.1.1-linux-x86_64/bin/`  [해제한 폴더로 이동]
3. `cp phantomjs /usr/local/bin/`  [해제한 내용을 해당 폴더에 카피하기]
4. `apt-get install -y fonts-nanum*` [나눔 한국어 폰트 다운로드]
5. `docker ps -a` [록을 확인해서 방금 들어온 도커의 컨테이너 id[48715bb423ab]를 확인]
6. `docker commit 48715bb423ab ubuntu-phantomjs` [당 컨테이너 아이디를 ubuntu-phantomjs 라는 아이디로 변경 후 저장(보기 쉽게)]

<br/>

---

<br/>

위의 절차를 따라 컨테이너를 만든 후 아래와 같이 **UTF-8** 설정들을 해줍니다.

이 설정이 없으면 이후에 한글이 제대로 출력이 되지 않기 때문에 꼭 해주어야 합니다.

`docker run -i -t -v /c/Users/Vector/sample:/sample -e ko_KR.UTF-8 -e PYTHONENCODING=utf_8 ubuntu-phantomjs /bin/bash`

<br/>


기존에 cmd창에서 파이썬 파일을 실행을 할 때 'python test.py' 란 명령어로 파일을 실행하였습니다.

하지만 이 컨테이너에선 기존에 사용하던 켄테이너와 달리 **python3** 버전을 사용했기 때문에 'python3 test.py' 으로 입력해야 됩니다.

![image](https://user-images.githubusercontent.com/57824945/132694982-4dbebfd9-dbea-4364-8a73-22cfbf58f00f.png)


도커 접속 코드 : docker run -i -t -v /c/Users/Vector/sample:/sample ubuntu-phantomjs /bin/bash
