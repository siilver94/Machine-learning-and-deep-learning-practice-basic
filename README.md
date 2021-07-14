# 딥러닝 실습

딥러닝 알고리즘을 어떻게 만드는 가가 아닌 딥러닝을 구현하는 것 보다는 구현 돼 있는 것을 활용하는 프로젝트

데이터를 어떻게 수집하고 알고리즘을 활용하여 내가 원하는 가치를 창출

머신러닝/ 딥러닝을 어떻게 사용하는가.

<br/>

## WEB으로의 요청

웹으로 요청을 걸 때 방식은 대표적으로 POST, PUT, DELETE 가 있습니다.

그 중 **GET** 방식은, 웹에서 페이지를 클릭을 하면 페이지를 이동하게 됩니다. 이게 곧 요청이고 요청을 할 때는
대상 그리고 추가적인 정보가 필요합니다. 추가적인 정보는 경로와 데이터로 나눌 수 있습니다.

<br/>

### 예

**방식** : GET, POST, PUT, DELETE

**대상** : [https://search.naver.com/](https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF) ⇒ 호스트 이름

**추가적인 정보** :   

  - 경로 : /[search.naver](https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF)

  - 데이터 : ?cid=318190

형태는 처음에 **?** 로 시작하여 `키=값` 형식이고 구분은 **&** 기호로 합니다.

```
?where=nexearch

&sm=top_hty

&fbm=1

&ie=utf8

&query=초콜릿
```

