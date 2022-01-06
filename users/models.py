from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="ایمیل",
        error_messages={"unique": "این ایمیل قبلا ثبت شده است."},
    )
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        default="default_profile.png",
        upload_to="profile_photos",
        verbose_name="عکس پروفایل",
    )
    receive_updates = models.BooleanField(
        default=False,
        verbose_name="دریافت آپدیت ها",
        help_text="با فعال کردن این گزینه هرگاه مقاله جدیدی در سایت منتشر شود ایمیل اطلاع رسانی برای شما ارسال خواهد شد.",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with Image.open(self.photo.path) as image:
            if image.height > 225 or image.width > 225:
                size = (225, 225)
                image.resize(size, Image.ANTIALIAS).save(self.photo.path)

    def __str__(self):
        return f"{self.user.username} Profile"
