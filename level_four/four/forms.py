from django import forms
from django.contrib.auth.models import User
from four.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class new_user(forms.ModelForm):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = '__all__'
