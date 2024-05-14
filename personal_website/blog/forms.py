# from django.forms import ModelForm
# from .models import Comment, ContactMessage


# class CommentForm(ModelForm):
#     """
#     A form used for storing new comments in database.
#     """
#     class Meta:
#         model = Comment
#         fields = ['comment']
#         labels = {
#             'comment': 'دیدگاه شما'
#         }


# class ContactForm(ModelForm):
#     """
#     A form used for storing user's messages to admins in database.
#     """
#     class Meta:
#         model = ContactMessage
#         fields = ['title', 'name', 'email', 'message']
#         labels = {
#             'title': 'عنوان',
#             'name': 'نام شما',
#             'email': 'ایمیل',
#             'message': 'پیام'
#         }
