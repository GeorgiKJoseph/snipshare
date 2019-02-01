from django.contrib import admin
from .models import Pastebin, Account, Vote

admin.site.register(Pastebin)
admin.site.register(Account)
admin.site.register(Vote)
# Register your models here.
