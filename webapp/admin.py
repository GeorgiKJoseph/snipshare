from django.contrib import admin
from .models import Pastebin, Account, Vote, UserAccount

admin.site.register(Pastebin)
admin.site.register(Account)
admin.site.register(Vote)
admin.site.register(UserAccount)
# Register your models here.
