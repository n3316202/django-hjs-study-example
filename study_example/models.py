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