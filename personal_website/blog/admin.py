from django.contrib import admin
from .models import Comment, Article
from django_summernote.admin import SummernoteModelAdmin
from .models import Article


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ("description", "content")
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Comment, CommentAdmin)
# admin.site.register(Quote)
# admin.site.register(ContactMessage)
