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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    login_time = models.DateTimeField(auto_now=True)

class antenna(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)     #天线id
    rec_beam = models.IntegerField(default=0)     #波束收
    available_rec_beam = models.IntegerField(default=0)     #剩余波束收
    create_time = models.DateTimeField(auto_now_add=True)     #创建时间
    login_time = models.DateTimeField(auto_now=True)     #最后登录时间
    mapping = models.TextField(default="{}")     #信道映射
    Beam_ava = models.TextField(default="{}")     #记录波束是否被占用

class server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)     #服务器id
    core = models.IntegerField(default=0)     #核心数
    GPU = models.IntegerField(default=0)     #加速卡数量
    available_GPU = models.IntegerField(default=0)     #剩余加速卡数量
    available_CORE = models.IntegerField(default=0)     #剩余核心数
    Ip_mapping = models.TextField(default="{}")     #服务器ip映射

class task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)     #任务id
    task_name = models.CharField(max_length=32)     #任务名
    beam_type = models.IntegerField(default=0)     #波束类型
    meta_task_num = models.IntegerField(default=0)     #元任务数量

class meta_task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)     #元任务id
    meta_task_name = models.CharField(max_length=32)     #元任务名
    core = models.IntegerField(default=0)     #元任务所需核心数
    GPU = models.IntegerField(default=0)     #元任务所需加速卡数量
    belong_task = models.ForeignKey(task, on_delete=models.CASCADE)     #所属任务id

class task_list(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)     #任务实例id
    task = models.ForeignKey(task, on_delete=models.CASCADE)     #外键到task，指明任务种类
    priority = models.IntegerField(default=0)     #任务优先级
    starttime = models.DateTimeField(auto_now_add=True)     #任务开始时间戳
    endtime = models.DateTimeField(auto_now=True)     #任务结束时间戳
    antenna = models.ForeignKey(antenna, on_delete=models.CASCADE)     #外键到Antenna表
    beam = models.IntegerField(default=0)     #使用该天线的波束号
    status = models.CharField(max_length=32)     #该任务的状态

class meta_task_list(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)     #任务实例id
    task_id = models.ForeignKey(task_list, on_delete=models.CASCADE)     #外键到task_list，指明该元任务所属的任务实例
    server = models.ForeignKey(server, on_delete=models.CASCADE)     #外键到server,该元任务所属的任务实例
    meta_task = models.ForeignKey(meta_task, on_delete=models.CASCADE)     #外键到meta_task,该元任务的类型

class log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)     #日志id
    type = models.CharField(max_length=32)     #日志类型
    time = models.DateTimeField(auto_now_add=True)     #时间戳
    info = models.TextField(default="{}")     #日志内容



# class admin(models.Model):
#     user = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     created_at = models.DateTimeField(auto_now_add=True)


# class tag(models.Model):
#     tag = models.CharField(max_length=20)
#     def __str__(self):
#         return str(self.tag)

# class manga(models.Model):
#     title=models.CharField(max_length=30, verbose_name="中文标题")
#     org_title = models.CharField(max_length=30, verbose_name="原始标题")
#     alternate_titles = models.CharField(max_length=40, blank=True,verbose_name="译名/其它译名",default="")
#     author=models.CharField(max_length=20,verbose_name="作者",default="")
#     tags = models.ManyToManyField(to=tag,verbose_name="标签", blank=True)#外键到tag
#     STATUS_CHOICES = [
#         ('连载中', '连载中'),
#         ('停更', '停更'),
#         ('完结', '完结'),
#         ('独立作品', '独立作品'),
#         ('衍生作品','衍生作品')
#     ]
#     status=models.CharField(max_length=10, choices=STATUS_CHOICES,default='SER',verbose_name="连载状态")
#     created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
#     review=models.TextField(verbose_name="我的想法", blank=True, null=True)
#     finish=models.BooleanField(default=False,verbose_name="完成阅读")
#     myprogress=models.CharField(max_length=20,verbose_name="我的进度", blank=True, null=True)
#     pic=models.ImageField(upload_to='Base/manga/pic', blank=True, null=True)


# Create your models here.
