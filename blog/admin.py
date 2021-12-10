from django.contrib import admin
from . models import Comment, Article, Quote, ContactMessage


class ArticleAdmin(admin.ModelAdmin):
    """
    In here we set author of article to the current user(admin) when the object is created on the admin panel.
    """

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


class CommentAdmin(admin.ModelAdmin):
    """
    In here we set author of comment to the logged in admin for any admin who tris to register a new comment on admin panel.
    """

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Quote)
admin.site.register(ContactMessage)
