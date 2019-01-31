from django import forms

from .models import Account, Pastebin

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user_name', 'email', 'password',)

class PastebinForm(forms.ModelForm):
    class Meta:
        model = Pastebin
        fields = ('author', 'title', 'language', 'code',)