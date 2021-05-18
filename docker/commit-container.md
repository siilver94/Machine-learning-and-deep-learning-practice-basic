## 컨테이너 상태 저장

<br/>


`docker run -i -t continuumio/miniconda3 /bin/bash`  명령어로  **miniconda3** 실행 합니다.

<br/>


#### 아래 명령어들을 입력하여 필요한 모듈을 다운로드 합니다.



`pip install beautifulsoup4`   beautifulsoup4  모듈 다운.

`pip install requests`   requests 모듈 다운.

<br/>

해당 모듈들을 다운 후 `exit` 명령어로 도커에서 나와 방금 설치한 **bs4 requests** 이미지 저장

`docker ps -a`  실행했던 것들이 나옴.

![image](https://user-images.githubusercontent.com/57824945/118590602-afcc7680-b7dd-11eb-87c0-7d01b4b67f8e.png)


<br/>

### 저장 하는 방법

docker commit <컨테이너 ID> <이름>:<태그>

`docker commit e83586765a8e mlearn:init`  를 입력하면 이미지 저장 완료.
