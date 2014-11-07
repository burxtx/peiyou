from django.db import models

# Create your models here.
class Employee(models.Model):
    """docstring for Employee"""
    # 基础模块，eHR员工数据接入
    user = models.OneToOneField(User,null=True, blank=True)
    email = models.EmailField(max_length=75, null=True, blank=True)
    # 福利模块，生日管理
    birtyday_lunar = models.DateField(null=True, blank=True)
    birtyday_solar = models.DateField(null=True, blank=True)
    # 年会视频模块
    addr = models.CharField(null=True, blank=True)
    # 培训模块，测试的最高分数
    exam_score = models.IntegerField(null=True, blank=True)

    # 员工级别，核心员工为？级以上
    grade = models.IntegerField(null=True, blank=True)

    openid = models.CharField(max_length=500, null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True)
    sex = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    headimgurl = models.CharField(max_length=500, null=True, blank=True)
    privilege = models.CharField(max_length=200, null=True, blank=True)
    subscribe_time = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return '%s, %s' % (self.nickname, self.openid)

class Family(object):
    """docstring for Family"""
    employee = models.ForeignKey(Employee)
    father = models.CharField(max_length=100, null=True, blank=True)
    mother = models.CharField(max_length=100, null=True, blank=True)
    kid1 = models.CharField(max_length=100, null=True, blank=True)
    kid2 = models.CharField(max_length=100, null=True, blank=True)
    kid3 = models.CharField(max_length=100, null=True, blank=True)
    def __unicode__(self):
        super(Family, self).__init__()
        self.arg = arg
        