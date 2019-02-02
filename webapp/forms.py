from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Account, Pastebin, Vote

class AccountForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
        )

    def save(self, commit=True):
        user= super(AccountForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user



class PastebinForm(forms.ModelForm):
    class Meta:
        model = Pastebin
        fields = ('title', 'language', 'code',)

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ()

class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('user_name','password',)

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )