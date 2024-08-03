## 폴더를 마운트해서 이미지 실행하기

<br/>


폴더를 마운트 한다는 것은 폴더를 끼워넣는다 라고도 표현하고, 외장하드에 연결한다 라고 생각 하면 됩니다.

**마운트 : 끼워 넣는다고 표현**

`$docker run -i -t -v <윈도우의 폴더>:<컨테이너의 폴더><이미지 이름>:<태그 이름>`

`docker run -i -t -v /c/Users/Vector/sample:/sample mlearn:init`
