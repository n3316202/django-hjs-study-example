from django.db import models
from django.db.models import TextChoices

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

#dev_3
class Posting(models.Model):
    owner_name = models.CharField(max_length=128, help_text="Name of posting owner")
    contents = models.CharField(max_length=32, help_text="Contents of posting")
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Creation time")
    modified_at = models.DateTimeField(auto_now=True, help_text="Last modified time")
    
    class Meta:
        db_table = "posting"
        get_latest_by = ("modified_at", "created_at")
        # modified_at 값이 가장 최신인 것이 가장 최신 Posting임.
        # 만약 modified_at의 값이 같다면, created_at 값을 기준으로 함.

#dev_4
# class Product(models.Model):
#     class ProductType(TextChoices):
#         GROCERY = "grocery", "식료품"
#         FURNITURE = "furniture", "가구"
#         BOOKS = "books", "책"
#         FOOD = "food", "음식"

#     name = models.CharField(max_length=128, help_text="상품명")
#     price = models.IntegerField(
#         help_text="상품 가격",
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#     )
#     product_type = models.CharField(choices=ProductType.choices, max_length=32)
#     store = models.ForeignKey(
#         to="stores.Store",
#         on_delete=models.CASCADE,
#         null=True,
#         help_text="이 상품을 판매하는 가게",
#         related_name="product_new",
#     )

#     class Meta:
#         db_table = "product"
#         db_table_comment = "상품 테이블 입니다."
#         ordering = ("-created_at",)
      
