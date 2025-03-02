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