from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 



class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    city = models.CharField(max_length=50,default='')
    phone = models.IntegerField(default=0)

def create_account(sender, **kwargs):
    if kwargs['created']:
        user_account= UserAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_account, sender=User)


class Pastebin(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    code = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    upvotes=models.IntegerField(default=0)


#    up_vote= ListCharField(
#        base_field=CharField(max_length=50),
#        max_length=(51*25)
#    )

    def __str__(self):
        return self.title

class Vote(models.Model):
    acc_pk=models.IntegerField()
    pastebin_pk=models.IntegerField()

#account model... 
class Account(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.user_name
