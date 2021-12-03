from django.db import models
from users.models import User
from django.utils.timezone import localtime
from persiantools.jdatetime import JalaliDateTime
from persiantools import digits
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):

    title = models.CharField(max_length=120)
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, editable=False)
    date_posted = models.DateTimeField(
        auto_now_add=True)
    description = models.TextField(max_length=250)
    image_1 = models.ImageField(
        upload_to='article-images/', default=None, blank=True)
    paragraph_1 = models.TextField(default=None, blank=True)
    image_2 = models.ImageField(
        upload_to='article-images/', default=None, blank=True)
    paragraph_2 = models.TextField(default=None, blank=True)
    image_3 = models.ImageField(
        upload_to='article-images/', default=None, blank=True)
    paragraph_3 = models.TextField(default=None, blank=True)
    image_4 = models.ImageField(
        upload_to='article-images/', default=None, blank=True)
    paragraph_4 = models.TextField(default=None, blank=True)
    image_5 = models.ImageField(
        upload_to='article-images/', default=None, blank=True)
    paragraph_5 = models.TextField(default=None, blank=True)
    image_6 = models.ImageField(
        upload_to='article-images/', default=None, blank=True)
    paragraph_6 = models.TextField(default=None, blank=True)
    image_7 = models.ImageField(
        upload_to='article-images/', default=None, blank=True)
    paragraph_7 = models.TextField(default=None, blank=True)
    image_8 = models.ImageField(
        upload_to='article-images/', default=None, blank=True)
    paragraph_8 = models.TextField(default=None, blank=True)

    def get_jalalidatetime(self):
        datetime = localtime(self.date_posted)
        return digits.en_to_fa(JalaliDateTime.to_jalali(datetime).strftime("%H:%M | %Y/%m/%d"))

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500)
    date_posted = models.DateTimeField(
        auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    parent = TreeForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    confirmed = models.BooleanField(default=False, blank=True)

    class MPTTMeta:
        order_insertion_by = ['date_posted']

    def get_jalalidatetime(self):
        datetime = localtime(self.date_posted)
        return digits.en_to_fa(JalaliDateTime.to_jalali(datetime).strftime("%H:%M | %Y/%m/%d"))

    def __str__(self):
        if self.confirmed:
            return f'Comment #{self.id} on Article {self.article}'
        else:
            return f'Unconfirmed Comment #{self.id} on Article {self.article}'


class Quote(models.Model):
    author = models.CharField(max_length=100)
    quote = models.TextField()
    identifier = models.CharField(max_length=100)

    def __str__(self):
        return self.identifier
