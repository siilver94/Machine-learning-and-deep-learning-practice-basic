## Docker 개발환경 구축

<br/>

**Docker toolbox**는 더 이상 지원되지 않으니, Docker 공식 홈페이지에서 **docker desktop** 를 다운로드 합니다.

[Docker 공식 홈페이지 ](https://www.docker.com/get-started)

**Docker** 설치 후, **CMD** 창에서 해당 문구를 입력 하였을때 아래와같은 글들이 뜨면 환경 설정이 완료 됩니다.

`docker run hello-world`


![image](https://user-images.githubusercontent.com/57824945/118384892-1bc7a700-b645-11eb-97bb-57f447cc102f.png)

<br/>

### Miniconda3

**Miniconda3**란, **우분투**를 깔아놓고 그 위에 **Anaconda**에서 인공지능에 관련된 기본적인 모듈을 잔뜩 모아놓은 미들웨어들을 설치한 이미지 입니다.

**Miniconda**란 간단히 말해 **파이썬 가상환경 관리 툴** 로 패키지들의 의존성을 관리하기 쉽게 해줍니다.

cmd창에 `docker pull continuumio/miniconda3`  입력

<br/>

### Docerk 이미지 

#### 이미지 가져오기

`docker pull(이미지 가져오기) continuumio(만든사람)/miniconda3(가져오려는 이미지)`

![image](https://user-images.githubusercontent.com/57824945/118384973-bd4ef880-b645-11eb-990f-572ce45f5bd2.png)

<br/>

#### 이미지 실행

이미지 실행 : `docker run -i -t continuumio/miniconda3 /bin/bash`


이미지를 실행하면 리눅스 환경이 되어 내부에서 리눅수 명령어 사용 가능.

![image](https://user-images.githubusercontent.com/57824945/118384993-f4250e80-b645-11eb-95cc-d13832f0e04e.png)



`python3 -c 'print(3*5)` 해당 리눅스 명령어를 사용하여 파이썬이 잘 사용되어 지는지 확인 가능.

`exit` 으로 가상환경 나가기 가능.

해당 환경에서는 무슨 짓을 해도 기존 **miniconda3환경에는 아무런 영향을 주지 않음.**

<br/>
