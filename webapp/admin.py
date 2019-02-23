from django.contrib import admin
from .models import Pastebin, Vote, Friend

admin.site.register(Pastebin)
#admin.site.register(Account)
admin.site.register(Vote)
#admin.site.register(UserAccount)
admin.site.register(Friend)
# Register your models here.
