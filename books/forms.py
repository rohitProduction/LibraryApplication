from django import forms
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator
from django.forms import fields,widgets
from django.utils import timezone

class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SignUpForm(forms.ModelForm):
    """Form enabling unregistered users to sign up."""

    class Meta:
        model = User
        fields = ['username', 'new_password', 'password_confirmation', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
        }

    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        validators=[RegexValidator(
            regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            )]
    )
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    def clean(self):
        """Clean the data and generate messages for any errors."""

        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Confirmation does not match password.')

    def save(self):
        """Create a new user."""

        super().save(commit=False)
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('new_password'),
        )
        return user
    
FILTER_CHOICES= [
    ('', ''),
    ('canBorrow', 'Available for borrowing'),
    ('dueToday', 'Due today'),
    ('onLoan', 'Currently on loan'),
    ]

"""Form to filter books"""
class FilterForm(forms.Form):
    filter= forms.CharField(label='Choose a filter', widget=forms.Select(choices=FILTER_CHOICES), required=False)
