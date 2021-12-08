from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, User


class LoginForm(AuthenticationForm):
    """
    We use this form in order to display labels and errors in persian instead of default AuthenticationForm's labels and forms.
    """

    username = forms.CharField(max_length=254, label=("نام کاربری"))
    password = forms.CharField(label=("رمز عبور"), widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': ("نام کاربری یا رمز عبور اشتباه است."),
        'inactive': ("این اکانت غیرفعال است."),
    }


class RegisterForm(UserCreationForm):
    """
    We use this form in order to display labels and errors in persian instead of default UserCreationForm's labels and forms.
    """

    username = forms.CharField(max_length=254, label=("نام کاربری"), error_messages={
        "unique": "این نام کاربری قبلا ثبت شده است."})
    password1 = forms.CharField(
        label="رمز عبور",
        strip=False,
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="تکرار رمز عبور",
        strip=False,
        widget=forms.PasswordInput)
    error_messages = {
        'password_mismatch': ("رمز عبورها باید دقیقا مثل هم باشند.")
    }

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
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
