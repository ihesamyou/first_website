from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Article(models.Model):
    """
    A model for admins to publish articles.
    """
    title = models.CharField(max_length=120)
    author = models.ForeignKey(
        User, null=False, on_delete=models.PROTECT, editable=False
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=250)
    metatag = models.TextField(max_length=450, default=None, blank=True)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.id})


class Comment(MPTTModel):
    """
    Comments for registered users.
    django-mptt is used for saving comments in a hierarchial manner and for
    retrieving them on article_detail template. see django-mptt docs for more.
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, editable=False)
    parent = TreeForeignKey(
        "self", null=True, blank=True, on_delete=models.PROTECT, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["date_posted"]

    def get_absolute_url(self):
        return reverse("comment", kwargs={"pk": self.article.pk})

    def __str__(self):
        return f"Comment #{self.id} on Article {self.article}"


# class Quote(models.Model):
#     """
#     A model that gets updated by celery's get_quote task using quote.py script.
#     celery's random_quote task will use data from this model to save a random quote to cache.
#     identifier field is used for removing the possibility of the same quote being saved to database twice.
#     """

#     author = models.CharField(max_length=100)
#     quote = models.TextField()
#     identifier = models.CharField(max_length=100)

#     def __str__(self):
#         return self.identifier


# class ContactMessage(models.Model):
#     """
#     Messages from users to Admins submitted in contact page.
#     get_jalalidatetime is used here to show the jalali datetime in name of each instance.
#     """

#     title = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField(max_length=3000)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.title} on {self.get_jalalidatetime()}"
