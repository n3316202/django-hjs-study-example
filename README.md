1.프로젝트 폴더 생성
mkdir django_hjs_study_example

2.장고 프로젝트 생성
django-admin startproject config .

3.study_example 앱 생성
python manage.py startapp study_example

4.앱 생성후 실행
python manage.py runserver

https://velog.io/@calzone0404/%ED%95%99%EC%8A%B5-%EC%A0%95%EB%A6%AC-Chapter-2.-%EB%AA%A8%EB%8D%B8%EB%A7%81%EA%B3%BC-%EB%A7%88%EC%9D%B4%EA%B7%B8%EB%A0%88%EC%9D%B4%EC%85%98-t28tx7xl

5. python manage.py makemigrations study_example

6. python manage.py migrate

####

장고 셀 작동 : python manage.py shell

장고셀 작동후 아래를 차례대로 작동
from study_example.models import Posting

Posting.objects.create(id=1,owner_name="홍길동",contents='')
Posting.objects.create(id=2,owner_name="여우랑",contents='')
Posting.objects.create(id=3,owner_name="안국진",contents='')

In [9]: Posting.objects.latest()
Out[9]: <Posting: Posting object (3)> # 여현구를 의미 - 가장 최근에 수정한 게시물을 가져온다.

In [10]: p = Posting.objects.get(id=1)

In [11]: p.owner_name = "홍철수"

In [12]: p.save()

In [13]: Posting.objects.latest()
Out[13]: <Posting: Posting object (1)> # 홍철수를 의미 - 가장 최근에 수정한 게시물을 가져온다.

### ordering 기본값 : None

Django ORM을 이용하여 데이터 조회 시 정렬 방법을 설정할 때 사용한다. 기본값으로 primary key (id)값으로 설정되어 있다.

### 장고 쿼리 보기

In [3]: q= Posting.objects.all()

In [4]: q.query
Out[4]: <django.db.models.sql.query.Query at 0x203d80edac0>

In [5]: str(q.query)
Out[5]: 'SELECT "posting"."id", "posting"."owner_name", "posting"."contents", "posting"."created_at", "posting"."modified_at" FROM "posting"'

# https://m.blog.naver.com/jun_d_/222031792162

# Django 모델 API (데이터를 추가/갱신/조회)

# insert : 객체생성후에 save() 함수를 이용하여 새객체를 insert한다.

# select : Django 모델 클래스에 대해 objects라는 Manager 객체를 자동으로 추가한다.

# objects는 django.db.models.Manager 이다. 이매니저 객체를 이용해서 데이터

# 필터링 할 수 있고, 정렬을 할 수 있으며 기타 여러 기능들을 사용할 수 있다.

# 데이터를 읽어올 때 바로 이 매니저 객체를 사용하였음(모델클래스.objects)

# all() : 테이블 데이터를 모두 가져온다. Question.objects.all()

# get() : 하나의 row만을 가져올 때 사용하는 메소드이다. Primary Key를 가져올때

# 는 Question.objects.get(pk = 1)

# filter() : 특정조건을 이용하여 Row들을 가져오기 위한 메소드

# exclude() : 특정 조건을 제외한 나머지 Row들을 가져오기 위한 메소드 filter()반대개념

# count() : 데이터의 갯수(row 수)를 세기위한 메소드

# order_by() : 데이터를 특정 키에 따라 정렬하기 위한 메소드, 정렬키를 인수로 사용하는데

      # -가 붙으면 내림차순이 된다.
      # Question.objects.order_by('-id')

# distinct() : 중복된 값은 하나로만 표시하기 위한 메소드, SQL의 SELECT DISTINCT와 같은

      # 같은 기능
      # rows = User.objects.distinct('name')

# first() : 여러개의 데이터중에서 처음에 있는 row만을 리턴한다.

      # rows = User.objects.order_by('name').first()
      # 위의 결과는 정렬된 레코드(row)중에서 가장 첫번째 row가 리턴값이 된다.

# last() : 여러개의 데이터중에서 마지막 row만을 리턴한다.

## 위의 메소드들은 실제 데이터 결과를 직접 리턴하기보다는 쿼리 표현식(QuersySet)으로

## 리턴한다.따라서, 여러 메소드들을 체인처럼 연결해서 사용할 수 있다.

## row = User.objects.filter(name = 'Lee').order_by('-id').first()

# update : 수정할 row객체를 얻은 후에 변경할 필드를 수정한다. 수정한 후에는 save() 메소드를

# 호출한다. SQL의 UPDATE가 실행되어 테이블에 데이터가 갱신된다.

# delete : Row객체를 얻어온 후에 delete() 메소드를 호출한다. delete메소드에 의해서

# 바로 데이터베이스의 레코드(row)가 삭제된다.
