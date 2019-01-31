from django.db import models
from django.conf import settings
from django.utils import timezone

class Pastebin(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=50,default='python')
    code = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

#account model... 
class Account(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
