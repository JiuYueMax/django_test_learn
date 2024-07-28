from django.db import models

# Create your models here.

# 定义班级的模型类，对应了数据库中的一张表
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDeleted = models.BooleanField(default=False)

# 学生模型类
class Student(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=50)
    isDeleted = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey(Grades)
