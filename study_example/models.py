from django.db import models


#dev_1
class Human(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        abstract = True
        # abstract=True 인 경우 db_table을 지정할 수 없습니다.


class Man(Human):
    class Meta:
        db_table = "man"


class Woman(Human):
    class Meta:
        db_table = "woman"

#dev_4
class Product(models.Model):
    class ProductType(models.TextChoices):
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#enumeration-types
        GROCERY = "grocery", "식료품"
        FURNITURE = "furniture", "가구"
        BOOKS = "books", "책"

    name = models.CharField(max_length=128, help_text="Product Name")
    price = models.IntegerField(help_text="Product Price")
    created_at = models.DateTimeField(auto_now_add=True)
    product_type = models.CharField(choices=ProductType.choices, max_length=32)

    class Meta:
        constraints = (
            models.CheckConstraint( # price는 무조건 0보다 크거나 같아야한다.
                check=models.Q(price__gte=0),
                name="price_gte_0"
            ),
            models.UniqueConstraint( # name과 product_type은 Unique해야 한다.
                fields=["name", "product_type"],
                name="unique_name_product_type"
            )
        )

# Create your models here.

class Movie(models.Model) :
  title             = models.CharField(max_length=45)
  release_date      = models.DateField()
  running_time_min  = models.IntegerField(null=True)
  actors            = models.ManyToManyField("Actor", db_table="movie_actor" )
  # 영화가 배우를 정참조 ↔ 배우는 영화를 역참조(_set)
  # through를 통해 DB내에 자동으로 생성되는 movie_actor 테이블 생성

  class Meta: 
    db_table = "movies"

class Actor(models.Model) :
  first_name    = models.CharField(max_length=45)
  last_name     = models.CharField(max_length=45)
  date_of_birth = models.DateField()

  class Meta : 
    db_table = "actors"

#dev_7
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

#dev_8

class Department(models.Model):
    deptno = models.PositiveSmallIntegerField(primary_key=True)
    dname = models.CharField(max_length=14)
    loc = models.CharField(max_length=13)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    empno = models.PositiveIntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    job = models.CharField(max_length=9)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    hiredate = models.DateField()
    sal = models.DecimalField(max_digits=7, decimal_places=2)
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    deptno = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

class SalaryGrade(models.Model):
    grade = models.PositiveIntegerField(primary_key=True)
    losal = models.PositiveIntegerField()
    hisal = models.PositiveIntegerField()

    def __str__(self):
        return f"Grade {self.grade}"
    