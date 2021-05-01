

간단하면서도 헷갈리는 개념 중 하나이다.

쉽게 말하면, 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스이다.

즉, 어플리케이션과 프로그래밍으로 소통하는 방법이다.

CLI와 GUI에서 각각 명령줄과 그래픽(아이콘)을 통해서 특정 기능을 수행하기 위하여,

API는 프로그래밍을 통해 그 일을 수행할 수 있다.

![image-20210502001101406](C:/Users/kimth/AppData/Roaming/Typora/typora-user-images/image-20210502001101406.png)



# Rest Api란?

Representational State Transfer

웹 설계 상의 장점을 최대한 활용 할 수 있는 아키텍처 방법론

네트워크 아키텍쳐 원리의 모음

Rest 원리를 따르는 시스템 혹은 API를 RESTful API라고 하기도 한다.

쉽게 말해서, '자원'과 '주소'를 지정하는 방법이다.



# REST 구성

- 자원(URI)
- 행위(HTTP Method)
- 표현(Representations)



# URI란?

Uniform Resource Identifier

통합 자원 식별자

인터넷의 자원을 나타내는 유일한 주소

인터넷에서 자원을 식별하거나 이름을 지정하는 데 사용되는 간단한 문자열

하위 개념: URL, URN

URN을 사용하는 비중이 매우 적기 때문에 일반적으로 URL은 URI를 통칭하는 말로 사용한다.

![image-20210502004203457](C:/Users/kimth/AppData/Roaming/Typora/typora-user-images/image-20210502004203457.png)



# URL

Uniform Resource Locator

통합 자원 위치

네트워크 상에 자원(리소스)이 어디 있는지(주소)를 알려주기 위한 약속

자원은 HTML 페이지, CSS 문서, 이미지 등이 될 수 있음

'웹 주소' 또는 '링크'라고도 불림



# URN

Uniform Resource Name

통합 자원 이름

URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함 (독립적 이름)

자원의 이름이 변하지 않는 한 자원의 위치를 이곳저곳 옮겨도 문제없이 동작



# HTTP Method

- 자원에 대한 행위
- 즉, HTTP는 HTTP Method를 정의하여 주어진 자원에 수행하길 원하는 행동을 나타낸다
- 의미론적으로 행위를 규정하기 때문에 '실제 그 행위 자체가 수행됨'을 보장하진 않는다
- HTTP verbs라고도 한다.



# HTTP Method 종류

-  GET

  - 특정 자원의 표시를 요청하며, 오직 데이터를 받기만 한다

    >**GET**, /articles/1/
    >
    >**GET**, /articles/

- POST

  - 서버로 데이터를 전송하며, 서버에 변경사항을 만든다

  - 데이터를 추가할 때, 주로 쓰인다

    > **POST**, /articles/

- PUT

  - 요청한 주소의 자원을 수정

    > **PUT**, /articles/1/

- DELETE

  - 지정한 자원을 삭제

    >**DELETE**, /articles/1/

- 이외에도 여러 Method가 있지만, 위 4가지가 가장 대표적이다.



# PUT과 PATCH Method의 차이

PUT과 PATCH는 자원을 수정한다는 공통점이 있지만,

수정하는 방식에 차이가 있다.

수정정보를 요청하게 될 때, 

PUT은 수정정보에 대한 정보만 수정되고, 나머지 정보는 기존 데이터로 유지한다.

반면, PATCH는 아예 모든 데이터가 초기화 되고, 수정정보가 입력된다.



# HTTP란?





# URL과 URN 비교 예시

- URL 예: '강원도 원주시 늘품로 아이파크'
- URN 예: '태이슨의 집'
- 만약 태이슨이 새로운 곳으로 이사를 가게 된다면,
  - 더 이상 '강원도 원주시 늘품로 아이파크'라는 주소(URL)로 찾을 수 없다
  - 새로운 주소(URL) '광주광역시 운암동 블루밍'으로 찾아야 한다
  - 하지만 URN인 '태이슨의 집'을 통해 태이슨의 집이 어디에 위치해 있는지 식별 가능하다
  - 즉, '태이슨의 집'이라는 고유한 이름(URN)은 변함이 없다
- URN은 자원의 ID를 정의하고, URL은 자원을 찾는 방법을 제공한다
- 따라서 URN과 URL은 상호 보완적이라고 할 수 있다.



# URI 설계 주의사항

- 가독성을 위해 언더바(_)가 아닌 하이픈(-)을 사용한다
- 대소문자에 따라 다른 자원으로 인식하게 되므로, 소문자만 사용한다
- 파일의 확장자는 포함시키지 않는다



# JSON

- JavaScript Object Notation
  - lightweight data-interchange format
  - 자바스크립트 객체 문법을 따르며, 구조화된 데이터를 표현하기 위한 문자 기반 데이터 포맷
  - 일반적으로 웹 어플리케이션에서 클라이언트로 데이터를 전송할 때 사용
- 다만, 자바스크립트 구문에 기반을 두고 있지만, JSON 그 자체로 자바스크립트는 아니다



# JSON 특징

- 사람이 읽고 쓰기 쉽고 기계가 파싱(해석&분석)하고 만들어 내기 쉬움
  - 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조
  - 쉽게 변환할 수 있는 key-value의 구조로 되어 있음
- 자바스크립트가 아니어도 JSON을 읽고 쓸 수 있는 기능이 다양한 프로그래밍 언어 환경에서 지원



# 파이썬에서의 JSON Parsing 

```python
import requests

URL = 'http://kobis.or.kr/kobisopenapi/webservice/rest..중략..json'
response - requests.get(URL)

# Dictionary로 Parsing
data = response.json()

# <class 'dict'>
print(type(data))
```



# REST 핵심 규칙

1. URI는 정보의 자원을 표현해야 한다.
2. 자원에 대한 (어떠한)행위는 HTTP Method로 표현한다.



# REST framework를 왜 사용할까?





















