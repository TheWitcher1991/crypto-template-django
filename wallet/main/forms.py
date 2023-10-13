from django import forms
from .models import Users


class RegisterForm(forms.Form, forms.ModelForm):
    email = forms.CharField(label="Email", required=True, widget=forms.EmailInput(attrs={"class": "popup__label-input"}))
    name = forms.CharField(label="Имя", required=True, min_length=4, widget=forms.TextInput(attrs={"class": "popup__label-input"}))
    password = forms.CharField(label="Пароль", required=True, min_length=8, widget=forms.PasswordInput(attrs={"class": "popup__label-input"}))
    '''lost = forms.CharField(label="Подтверждение пароля", required=True, widget=forms.TextInput(attrs={"class": 
    "popup__label-input"}))'''

    class Meta:
        model = Users
        fields = ['email', 'name', 'password']


class AuthForm(forms.Form):
    email = forms.CharField(label="Email", required=True, widget=forms.EmailInput(attrs={"class": "popup__label-input"}))
    password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput(attrs={"class": "popup__label-input"}))