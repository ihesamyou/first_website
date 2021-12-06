from django.forms import ModelForm
from .models import Comment, ContactMessage


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': 'دیدگاه شما'
        }


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['title', 'name', 'email', 'message']
        labels = {
            'title': 'عنوان',
            'name': 'نام شما',
            'email': 'ایمیل',
            'message': 'پیام'
        }
