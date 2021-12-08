from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, User


class LoginForm(AuthenticationForm):
    """
    We use this form in order to display labels and errors in persian instead to default AuthenticationForm.
    """

    username = forms.CharField(max_length=254, label=("نام کاربری"))
    password = forms.CharField(label=("رمز عبور"), widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': ("نام کاربری یا رمز عبور اشتباه است."),
        'inactive': ("این اکانت غیرفعال است."),
    }


class RegisterForm(UserCreationForm):
    """
    We use this form in order to display labels and errors in persian instead to default UserCreationForm.
    """
    password1 = forms.CharField(
        label="رمز عبور",
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html())

    password2 = forms.CharField(
        label="تکرار رمز عبور",
        strip=False,
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'username': 'نام کاربری',
            'email': 'ایمیل'
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'receive_updates']
