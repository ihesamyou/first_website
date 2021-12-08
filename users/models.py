from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, error_messages={
        "unique": "این ایمیل قبلا ثبت شده است."
    })
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        default='default_profile.png', upload_to='profile_photos')
    receive_updates = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
