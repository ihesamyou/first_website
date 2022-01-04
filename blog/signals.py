from django.dispatch import receiver
from django.db.models.signals import post_save
from blog.models import Article
from users.models import User
from django.core.mail import send_mass_mail
from django.urls import reverse


@receiver(post_save, sender=Article)
def article_notification(sender, instance, created, **kwargs):
    """
    When a new article is saved, Sends email to all users who have set their receive_updates=True.
    """
    if created:
        users = User.objects.filter(receive_updates=True)

        if users:
            emails = []
            for user in users:
                emails.append(user.email)

            subject = f"مقاله جدید"
            message = f'''
            مقاله جدیدی در سایت ihosseinu.com منتشر شده است.
            '{instance.title}'
            میتوانید از طریق لینک زیر مقاله را مشاهده کنید.

            {reverse('article-detail', kwargs={'pk':instance.id})}

             '''
            from_email = 'ihosseinu.com'

            send_mass_mail((subject, message, from_email, emails))
