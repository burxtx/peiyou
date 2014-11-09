from django.db import models
from django.conf import settings
from Employee import *
# Create your models here.

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

class UserProfile(models.Model):
    """docstring for UserProfile"""
    userprofile = models.ForeignKey(Employee)
    def __unicode__(self):
        return self.paper_name

class Paper(models.Model):
    """docstring for Paper"""
    paper_name = models.CharField(max_length=100)
    paper_desc = models.CharField(max_length=200,null=True,blank=True)
    paper_type = models.IntegerField(null=True,blank=True,verbose_name="paper type")
    def __unicode__(self):
        return self.paper_name


class Question(models.Model):
    """docstring for Question"""
    question_desc = models.CharField(max_length=200)
    question_index = models.IntegerField(null=True,blank=True,verbose_name="index")
    question_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="question type")
    paper = models.ForeignKey(Paper, null=True,blank=True)
    # 多选是多对多关系
    # correct = models.ManyToMany(Choice, null=True, blank=True)
    # 单选是多对一关系
    correct_value = models.ForeignKey(Value, null=True, blank=True)
    correct_choice = models.ForeignKey(Choice, null=True, blank=True)
    def __unicode__(self):
        return self.question_desc

class Value(models.Model):
    """docstring for Choice"""
    # question = models.ForeignKey(Question, null=True, blank=True)
    value_desc = models.CharField(max_length=100)
    value_index = models.IntegerField(choices=OPTION_CHOICE, null=True, blank=True, verbose_name="index")
    votes = models.IntegerField(default=0, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.choice_desc

class Choice(models.Model):
    """docstring for Choice"""
    # question = models.ForeignKey(Question, null=True, blank=True)
    value = models.ForeignKey(Value, null=True, blank=True)
    choice_desc = models.CharField(max_length=100)
    choice_index = models.IntegerField(choices=OPTION_CHOICE, null=True, blank=True, verbose_name="index")
    votes = models.IntegerField(default=0, null=True, blank=True)
    optional_text = models.CharField(max_length=300, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.choice_desc

class AnswerSheet(models.Model):
    """docstring for AnswerSheet"""
    paper = models.ForeignKey(Paper, null=True, blank=True)
    userprofile = models.ForeignKey(UserProfile, null=True, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(null=True, blank=True)
    # def __unicode__(self):
    #     return self.choice

class Answer(models.Model):
    """docstring for Answer"""
    answersheet = models.ForeignKey(AnswerSheet, null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True)
    # 多选是多对多关系
    # choice = models.ManyToMany(Choice, null=True, blank=True)
    # 多选是多对一关系
    value = models.ForeignKey(Value, null=True, blank=True)
    choice = models.ForeignKey(Choice, null=True, blank=True)
    userprofile = models.ForeignKey(UserProfile, null=True, blank=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    # def __unicode__(self):
    #     return self.choice

