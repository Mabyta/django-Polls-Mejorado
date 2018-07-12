from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import math
from django.db import models
from django.utils.html import mark_safe
from django.utils.text import Truncator
from markdown import markdown


class User_Polls(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)
    role = models.CharField(max_length=100)
    security_question = models.CharField(max_length=100)
    security_answer = models.CharField(max_length=100)
    
    
class Polls(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    pub_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
   
class Choices(models.Model):
    choice_text = models.CharField(max_length=100)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)
    
class Comments(models.Model):
    comment_text = models.CharField(max_length=100)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')