from django.db import models
from users.models import User
from django.utils.timezone import localtime
from persiantools.jdatetime import JalaliDateTime
from persiantools import digits
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Article(models.Model):
    """A model for admin users to publish articles. 8 separate paragraphs are provided for showing images
    between paragraphs if needed. get_jalalidatetime function will turn Gregorian datetime to jalalai datetime."""

    title = models.CharField(max_length=120)
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, editable=False)
    date_posted = models.DateTimeField(
        auto_now_add=True)
    description = models.TextField(max_length=250)
    metatags = models.TextField(max_length=450, default=None, blank=True)
    image_1 = models.ImageField(
        upload_to='article_images/', default=None, blank=True)
    paragraph_1 = models.TextField(default=None, blank=True)
    image_2 = models.ImageField(
        upload_to='article_images/', default=None, blank=True)
    paragraph_2 = models.TextField(default=None, blank=True)
    image_3 = models.ImageField(
        upload_to='article_images/', default=None, blank=True)
    paragraph_3 = models.TextField(default=None, blank=True)
    image_4 = models.ImageField(
        upload_to='article_images/', default=None, blank=True)
    paragraph_4 = models.TextField(default=None, blank=True)
    image_5 = models.ImageField(
        upload_to='article_images/', default=None, blank=True)
    paragraph_5 = models.TextField(default=None, blank=True)
    image_6 = models.ImageField(
        upload_to='article_images/', default=None, blank=True)
    paragraph_6 = models.TextField(default=None, blank=True)
    image_7 = models.ImageField(
        upload_to='article_images/', default=None, blank=True)
    paragraph_7 = models.TextField(default=None, blank=True)
    image_8 = models.ImageField(
        upload_to='article_images/', default=None, blank=True)
    paragraph_8 = models.TextField(default=None, blank=True)

    def get_jalalidatetime(self):
        datetime = localtime(self.date_posted)
        return digits.en_to_fa(JalaliDateTime.to_jalali(datetime).strftime("%H:%M | %Y/%m/%d"))

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    """Comments for registered users.
    django-mptt is used for saving comments with their children(replies) and also for
    retrieving them on article_detail template. see django-mptt docs for more.
    confirmed field is for admins to cofirm the comments before displaying them on the site.
    get_jalalidatetime function will turn Gregorian datetime to jalalai datetime."""

    article = models.ForeignKey(
        Article, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500, verbose_name=('دیدگاه شما'))
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

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.article.pk})

    def __str__(self):
        if self.confirmed:
            return f'Comment #{self.id} on Article {self.article}'
        else:
            return f'Unconfirmed Comment #{self.id} on Article {self.article}'


class Quote(models.Model):
    """A model that gets updated by celery's get_quote task using quote.py script.
    celery's random_quote task will use data from this model to save a random quote to cache.
    identifier field is used for removing the possibility of the same quote being saved to database twice."""

    author = models.CharField(max_length=100)
    quote = models.TextField()
    identifier = models.CharField(max_length=100)

    def __str__(self):
        return self.identifier


class ContactMessage(models.Model):
    """Messages from users to Admins submitted in contact page.
    get_jalalidatetime is used here to show the jalali datetime in name of each instance."""

    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)

    def get_jalalidatetime(self):
        datetime = localtime(self.date)
        return digits.en_to_fa(JalaliDateTime.to_jalali(datetime).strftime("%H:%M | %Y/%m/%d"))

    def __str__(self):
        return f'{self.title} on {self.get_jalalidatetime()}'
