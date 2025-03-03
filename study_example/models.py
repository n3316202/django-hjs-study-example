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


# In [4]: from study_example.models import Product

# In [5]: Product.objects.create(id=1,name="사과",price=1000)
# Out[5]: <Product: Product object (1)>

# In [6]: Product.objects.create(id=1,name="사과",price=-100)


#[Django] QuerySet에서 사용하는 '__'의 의미
#https://kimcoder.tistory.com/589

#1.첫번째 의미
#- exact, contains, in, gt, lt, startswith 등과 같은 필드 룩업을 사용하겠다는 의미 = where 조건절을 의미

#https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups 참고

##예)
#- exact  = is null

#Entry.objects.get(id__exact=14)
#Entry.objects.get(id__exact=None)

#SELECT ... WHERE id = 14;
#SELECT ... WHERE id IS NULL;

#2.두번째 의미

#2. 외래키 모델 속성 참조
#- 외래키 모델의 속성을 참조할 때에도 속성명 앞에 '__'를 붙인다.

# 예시

# 다음과 같이 Employee의 외래키를 User로 지정했다고 하자. 속성명은 user다.

# class Employee(models.Model):
#     ...
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
# User 객체의 username 속성값이 mark인 객체를 찾으려면 다음과 같이 접근하면 된다.

# Employee.objects.filter(user__username = 'Kim Jooyeok')
 

 

# 참고로, 위에서 설명한 두가지 방법을 한 번에 같이 사용할 수도 있다. 아래 예시에서는 User 객체의 username이 'Kim'으로 시작하는 Employee 객체들을 반환한다.

# Employee.objects.filter(user__username__startswith = 'Kim')