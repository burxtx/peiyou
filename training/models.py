from django.db import models

A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
J = 10
OPTION_CHOICE = (
    (A, "A"),(B, "B"),(C, "C"),(D, "D"),(E, "E"),(F, "F"),
    (G, "G"),(H, "H"),(I, "I"),(J, "J"),)
# Create your models here.
class Paper(models.Model):
    """docstring for Poll"""
    paper_name = models.CharField(max_length=100)
    paper_desc = models.CharField(max_length=200,null=True,blank=True)
    ptype = models.IntegerField(null=True,blank=True,verbose_name="paper type")
    def __unicode__(self):
        return self.paper_name

class Question(models.Model):
    """docstring for Question"""
    question_desc = models.CharField(max_length=200)
    qindex = models.IntegerField(null=True,blank=True,verbose_name="index")
    qtype = models.CharField(max_length=100, null=True, blank=True, verbose_name="question type")
    paper = models.ForeignKey(Paper)
    correct_1st = modesl.IntegerField(choices=OPTION_CHOICE)
    correct_2nd = modesl.IntegerField(choices=OPTION_CHOICE, null=True, blank=True, verbose_name="答案二")
    correct_3rd = modesl.IntegerField(choices=OPTION_CHOICE, null=True, blank=True, verbose_name="答案三")
    correct_4th = modesl.IntegerField(choices=OPTION_CHOICE, null=True, blank=True, verbose_name="答案四")
    correct_5th = modesl.IntegerField(choices=OPTION_CHOICE, null=True, blank=True, verbose_name="答案五")
    def __unicode__(self):
        return self.question_desc

class Choice(models.Model):
    """docstring for Choice"""

    question = models.ForeignKey(Question)
    choice_desc = models.CharField(max_length=100)
    cindex = models.IntegerField(choices=OPTION_CHOICE, null=True, blank=True, verbose_name="index")
    votes = models.IntegerField(default=0, null=True, blank=True)
    optional_text = models.CharField(max_length=300, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.choice_desc

class PollUser(models.Model):
    """docstring for PollUser"""
    MALE = 1
    FEMALE = 0
    GENDER_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        )
    LT35 = 1
    ST35 = 0
    AGE_CHOICE = (
        (LT35, 'Large'),
        (ST35, 'Small'),
        )
    # username = models.CharField()
    age = models.IntegerField(choices=AGE_CHOICE, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICE, null=True, blank=True)

    # subscribe = models.IntegerField()
    openid = models.CharField(max_length=500, null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True)
    sex = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    # language = models.CharField(max_length=100, null=True, blank=True)
    headimgurl = models.CharField(max_length=500, null=True, blank=True)
    privilege = models.CharField(max_length=200, null=True, blank=True)
    # subscribe_time = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return '%s, %s' % (self.age, self.gender)
 
class Answer(models.Model):
    """docstring for Answer"""
    pid = models.ForeignKey(Poll)
    qid = models.ForeignKey(Question)
    cid = models.ForeignKey(Choice)
    uid = models.ForeignKey(PollUser)
    submit_time = models.DateTimeField(auto_now_add=True)
    #add answer date and time
    def __unicode__(self):
        return self.cid