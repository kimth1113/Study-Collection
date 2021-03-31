# 장고 프로젝트 초기 설정

---

1. 프로젝트에서 사용할 패키지는 이 `venv` 내에서 관리 선언

   ```bash
   $ python -m venv venv
   ```

   (***주의 !*** 아직 활성화되지 않았음)

   ***tip***. 어떠한 패키지를 설치하면 저장되는 경로 명령어:  `which pip`	

2. `venv` 활성화

   ``` bash
   $ source venv/Scripts/activate
   ```

   (터미널을 켤 때마다 계속 실행해줘야함)

   ***tip.*** 명령어 간소화하기

   > 1. vim 공간 확인 명령어 `vi ~/.bash_profile`
   > 2. `i` 입력 후 `alias activate="source venv/Scripts/activate"` : 간소화 명령어 생성 
   > 3. `esc `, `:wq`, `Enter` 차례로 입력 후 기존 터미널 복귀
   > 4. 간소화 명령어 활성화 `source ~/.bash_profile`

3. 비어있는 `venv`에 필요한 패키지 설치

   ```bash
   $ pip install django
   ```

   > Django, django-bootstrap-v5, django-extensions, ipython 등

4. `.gitignore` 파일 생성 : 로컬 컴퓨터에서 쓰고 있는 패키지에 영향을 받지 않기 위함

   >구글 'gitignore.io' 검색 - 필요없는 패키지 검색 - 전체복사
   >
   >`manage.py`와 같은 레벨에 `.gitignore` 파일 생성 (가장 상위 폴더)
   >
   >**/taehyun.py : (어떤 경로에 있던지) 깃으로 관리하지 않음

5. 프로젝트에서 사용하고 있는 패키지 목록 저장

   ```bash
   $ pip freeze > requirements.txt
   ```

   >목록을 항상 외우고 다닐 수 없기 때문에..
   >
   >협업 시 다른 사람들을 배려하기 위해..

   ***tip.*** `pip install -r requirements.txt` : 패키지 목록 내 모든 패키지 설치

<br>

# 초기 파일 세팅

---

1. 프로젝트 파일 `config` 생성 

   ```bash
   $ django-admin startproject config .
   ```

2.  앱 생성 (앱 이름은 `articles`, `accounts`, `pages` 등)

   ```bash
   $ python manage.py startapp articles
   ```

   (***주의 !*** 앱 이름은 반드시 복수형으로)

3. (accounts 앱 생성 경우) **Custom User Model 설정**

   ```python
   # models.py
   from django.db import models
   from django.contrib.auth.models import AbstractUser
   
   # Create your models here.
   class User(AbstractUser):
       pass
   
   # settings.py 
   AUTH_USER_MODEL = 'accounts.User'
   ```

   > **새로운 프로젝트를 시작할 경우 기본 사용자 모델로도 충분하지만 기본적으로 사용자 지정 모델을 설정 하는것이 좋다. 확장이 용이 하여 필요에 따라 사용자에 대한 정의를 추가 할수 있기 때문이다.** 이유는 미래에 기본 사용자 모델을 사용하다가 필드를 추가할 경우 그것을 장고가 마이그레이션을 해주는 것이 불가능하기 때문이다. 많은 데이터들을 직접 수정해야 한다. **그래서 프로젝트를 만들고 제일 처음 하는일이 사용자 지정 유저 모델을 만드는 것이 좋다**.
   >
   > 검색: django custom user model
   >
   > 과정: 장고 공식 문서, abstractuser 검색

4. `models.py`에서 모델링 후

   ```python
   python manage.py makemigrations
   python manage.py migrate
   python manage.py showmigrations
   ```

   ***tip.*** `&&`을 통해 연속 명령 가능

   >`python manage.py makemigrations && python manage.py migrate` : 마이그레이션 생성 후 등록을 한번에

5. admin 페이지에 모델 추가

   ```python
   # admin.py
   from .models import Article
   ...
   admin.site.register(Article)
   ```

<br>

### 유용한 TIP 메모

---

- `urls.py` 에서 `app_name` 지정

  > 여러 앱의 `urls.py`에 같은 이름의 함수 지정( `views.함수이름` )이 있을 때, 구분하기 위해서..

- 왜 templates 폴더 내 앱 폴더를 또 만들어주는가?

  >여러 앱의 템플릿에 같은 이름의 html 파일이 있을 때, 구분하기 위해서..

- 변수 지정

  >`articles = Article.objects.all()` 또는 `article_list = Article.objects.all()`

- `views.py`에서 함수 사이 두 칸을 띄어주는 이유

  >pep8 파이썬 스타일 가이드에 있는 일종의 제안서 (개발자들의 관습(convention), 가독성을 위해)

- `request.GET` : 폼으로부터 전해받은 딕셔너리

- `'articles/'`와 `'/articles/'`의 차이

  ```
  # 현재 경로 : http://8000:/ssafy/
  
  # articles/ => 현재 경로부터 이어나감
  redirect('articles/')  
  # http://8000:/ssafy/articles/
  
  # /articles/ => 루트 경로부터 이어나감
  redirect('/articles/')  
  # http://8000:/articles/
  ```

- `html` 파일 내 `<input name="title">`, `<input name="content">` 에서 `name` 은 어디로 전달되는가?

  > `request.POST.get('title')` <= 여기 있는 `'title'`
  >
  > `request.POST.get('content')` <= 여기 있는 `'content'`





















