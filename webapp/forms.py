from django import forms

from .models import Account, Pastebin, Vote

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user_name', 'email', 'password',)

class PastebinForm(forms.ModelForm):
    class Meta:
        model = Pastebin
        fields = ('author', 'title', 'language', 'code',)

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ()

class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user_name','password',)