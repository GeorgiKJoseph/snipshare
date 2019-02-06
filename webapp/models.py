from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        if current_user != new_friend:
            friend.users.add(new_friend)

 
    @classmethod
    def lose_friend(cls,current_user,new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)


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

    def __str__(self):
        return self.title

class Vote(models.Model):
    users=models.ManyToManyField(User, null=True, blank=True)
    current_pastebin = models.ForeignKey(Pastebin,on_delete=models.CASCADE, related_name='current_bin', null=True)

    @classmethod
    def upvote(cls,current_pastebin,current_user):
        vote, created = cls.objects.get_or_create(
            current_pastebin=current_pastebin
        )
        vote.users.add(current_user)
    
    @classmethod
    def downvote(cls,current_pastebin,current_user):
        vote, created = cls.objects.get_or_create(
            current_pastebin=current_pastebin
        )
        vote.users.remove(current_user)



#    up_vote= ListCharField(
#        base_field=CharField(max_length=50),
#        max_length=(51*25)
#    )



#account model... 
class Account(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.user_name
