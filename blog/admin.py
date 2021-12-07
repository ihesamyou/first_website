from django.contrib import admin
from . models import Comment, Article, Quote, ContactMessage


class ArticleAdmin(admin.ModelAdmin):
    """In here we set author of articles to the current user for any admin who tris to publish a new article in admin panel."""

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


class CommentAdmin(admin.ModelAdmin):
    """In here we set author of comments to the current user for any admin who tris to register a new comment in admin panel."""

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Quote)
admin.site.register(ContactMessage)
