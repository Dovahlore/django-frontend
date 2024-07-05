
from django.db import models

# Create your models here.

#todo 建立数据库
class admin(models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    






# Create your models here.
