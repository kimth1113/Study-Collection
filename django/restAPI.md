# Rest Api란?

- REST: 웹의 장점을 최대한 최대한 활용할 수 있는 아키텍처(구조 또는 원리)
- REST의 핵심 규칙을 성실히 지킨 API를 'Rest Api'라고 함
- Rest는 'Representational State Transfer'의 약어



# REST 핵심 규칙

1. **URI**는 정보의 자원
2. 자원에 대한 행위는 **HTTP Method**로 표현



# URI란?

크게 URL과 URN으로 나뉨

Uniform Resource Identifier의 약어

- URL(Uniform Resource Locator)
  - 네트워크 상에서 자원의 위치
  - 흔히 말하는 '웹 주소' 또는 '링크'
- URN(Uniform Resource Name)
  - 자원의 이름

---

>URL, URN 쉬운 설명 
>
>- URL 예: '강원도 원주시 늘품로 아이파크'
>- URN 예: '태이슨 하우스'
>- 최초방문자도 URL을 통해 태이슨의 집을 쉽게 찾을 수 있음
>- 만약 태이슨이 새로운 곳(광주광역시)으로 이사를 가게 되면,
>   - 기존 주소(URL)로 태이슨의 집을 찾을 수 없음
>   - 하지만 '태이슨하우스'라는 고유한 이름(URN)은 변함이 없기 때문에,
>   - URN을 통해 태이슨의 집의 위치 식별 가능
>- 즉, URN과 URL은 상호보완적인 관계



# HTTP Method 종류

여러 종류가 있지만, 주로 5가지 Method 사용

- GET

  - 특정 자원을 표시
  - 수정 및 삭제 불가능

  > **GET** | '/movies/' => 전체 영화 정보 조회
  >
  > **GET** | '/movies/1/' => 특정 영화 정보 조회

- POST

  - 새로운 자원을 생성
  - API 서버로 새 데이터를 전송

  > **POST** | '/movies/' => 새로운 영화 추가

- PUT

  - 자원의 전체 정보를 수정
  - API 서버로 수정할 데이터를 전송

  > **PUT**, /movies/1/ => 1번 ID 영화 정보 수정

- PATCH

  - 자원의 일부 정보를 수정
  - API 서버로 수정할 데이터를 전송

  > **PATCH**, /movies/1/ => 1번 ID 영화 정보 수정

- DELETE

  - 자원을 삭제

  > **DELETE**, /articles/1/ => 1번 ID 영화 삭제

---

> PUT과 PATCH Method 기능은 자원을 수정한다는 공통점이 있지만,
>
> 수정하는 방식에 차이가 있다.
>
> API 서버에 정보 수정을 요청하게 될 때,
>
> PUT Method는 자원의 전체가 수정 정보로 교체된다.
>
> 반면, PATCH는 기존의 정보를 유지하면서 자원의 일부만 수정된다.



# 정리

오해하지말자. Rest API는 프레임워크나 라이브러리가 아니라 방법 및 구조이다.

여러 개발자가 서버와 데이터를 주고 받을 수 있도록, 최대한으로 표준화한 방법이다. 

Rest API의 구성요소에는 크게 자원과 행위가 있다.

자원은 우리가 보고 있는 페이지를 구성하고 있는 모든 데이터이다.

예를 들면, 직접적으로 페이지에서 볼 수 있는 그래프나 이미지도 자원이고,

그래프나 이미지를 구성하는 데이터도 자원이다.

그리고 그러한 데이터를 요청, 수정, 삭제 등의 처리를 할 수 있는데, 

이것을 행위의 종류라고 할 수 있다.

Rest를 형용사처럼 덧붙여 'Restful API'라고도 한다.





