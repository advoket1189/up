from django import forms
from django.contrib.auth.models import User
from .models import Profile

PARISH = (
    ('', 'Choose...'),
    ('St. Andrew', 'Kingston'),
    ('Portland ', 'St. Thomas'),
    ('St. Catherine', 'St. Mary'),
    ('St. Ann', 'Manchester',),
    ('Clarendon', 'Hanover',),
    ('Westmoreland', 'St. James',),
    ('Trelawny', 'St. Elizabeth')
)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                           'name': "password1",
                                                                                           'type': "password"}))


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                           'name': "password1",
                                                                                           'type': "password"}))
    password_confirm = forms.CharField(max_length=30, required=True,
                                       widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'name': "password2",
                                                                     'type': "password"}))
    TRN = forms.CharField(max_length=9, required=True, )
    address = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Parish = forms.ChoiceField(choices=PARISH)
    Agree = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm', 'address', ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        """Check if both password matches"""
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo',)
