from django import forms
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .models import Profile, User


class LoginForm(AuthenticationForm):
    """
    We use this form in order to display labels and errors in Farsi instead of default AuthenticationForm's labels and forms.
    """

    username = forms.CharField(max_length=254, label=("نام کاربری"))
    password = forms.CharField(label=("رمز عبور"), widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': ("نام کاربری یا رمز عبور اشتباه است."),
        'inactive': ("این اکانت غیرفعال است."),
    }


class RegisterForm(UserCreationForm):
    """
    We use this form in order to display labels and errors in Farsi instead of default UserCreationForm's labels and forms.
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
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل'
        }


class PasswordChange(PasswordChangeForm):
    """
    We use this form in order to display labels and errors in Farsi instead of default PasswordChangeForm's labels and forms.
    """

    old_password = forms.CharField(label=("رمز عبور فعلی"),
                                   widget=forms.PasswordInput)
    new_password1 = forms.CharField(label=("رمز عبور جدید"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("تکرار رمز عبور جدید"),
                                    widget=forms.PasswordInput)
    error_messages = {
        'password_mismatch': ("هر دو رمز عبور باید دقیقا مثل هم باشند."),
        'password_incorrect': ("رمز عبور فعلی اشتباه است.")
    }


class PasswordReset(PasswordResetForm):
    """
    We use this form in order to display labels and errors in Farsi instead of default PasswordResetForm's labels and forms.
    """
    email = forms.EmailField(label=("ایمیل"), max_length=254)


class ConfirmPasswordReset(SetPasswordForm):
    """
    We use this form in order to display labels and errors in Farsi instead of default PasswordChangeForm's labels and forms.
    """

    new_password1 = forms.CharField(label=("رمز عبور جدید"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("تکرار رمز عبور جدید"),
                                    widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل'
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'receive_updates']
        labels = {
            'photo': 'عکس',
            'receive_updates': 'دریافت آپدیت ها'
        }
