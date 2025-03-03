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


