from django.db import models

# Create your models here.
class Employee(models.Model):
    """docstring for Employee"""
    email = models.EmailField()
    age = models.IntegerField(choices=AGE_CHOICE, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICE, null=True, blank=True)

    # subscribe = models.IntegerField()
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
        return '%s, %s' % (self.nickname, self.)