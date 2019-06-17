from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError



class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(label='Enter email', required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(label='Enter password', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', required=True, widget=forms.PasswordInput)


    def clean_email(self):
        email = self.cleaned_data['email']
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user