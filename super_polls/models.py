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
    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)
    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 5
    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)
   
class Choices(models.Model):
    choice_text = models.CharField(max_length=100)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)
    
class Comments(models.Model):
    comment_text = models.TextField(max_length=4000)
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))