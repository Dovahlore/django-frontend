from django.db import models
import uuid
from django.db import models
from PIL import Image,ImageOps
from PIL.ExifTags import TAGS
import datetime
import os
# Create your models here.

#todo 建立数据库
class admin(models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)


class tag(models.Model):
    tag = models.CharField(max_length=20)
    def __str__(self):
        return str(self.tag)

class manga(models.Model):
    title=models.CharField(max_length=30, verbose_name="中文标题")
    org_title = models.CharField(max_length=30, verbose_name="原始标题")
    alternate_titles = models.CharField(max_length=40, blank=True,verbose_name="译名/其它译名",default="")
    author=models.CharField(max_length=20,verbose_name="作者",default="")
    tags = models.ManyToManyField(to=tag,verbose_name="标签", blank=True)#外键到tag
    STATUS_CHOICES = [
        ('连载中', '连载中'),
        ('停更', '停更'),
        ('完结', '完结'),
        ('独立作品', '独立作品'),
        ('衍生作品','衍生作品')
    ]
    status=models.CharField(max_length=10, choices=STATUS_CHOICES,default='SER',verbose_name="连载状态")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    review=models.TextField(verbose_name="我的想法", blank=True, null=True)
    finish=models.BooleanField(default=False,verbose_name="完成阅读")
    myprogress=models.CharField(max_length=20,verbose_name="我的进度", blank=True, null=True)
    pic=models.ImageField(upload_to='Base/manga/pic', blank=True, null=True)
# Create your models here.
