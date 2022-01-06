from django.dispatch import receiver
from django.db.models.signals import post_save
from blog.models import Article
from users.models import Profile
from django.core.mail import send_mass_mail
from django.urls import reverse


@receiver(post_save, sender=Article)
def article_notification(sender, instance, created, **kwargs):
    """
    When a new article is saved, Sends email to all users who have set their receive_updates=True.
    """
    if created:
        profiles = Profile.objects.filter(receive_updates=True)

        if profiles:
            emails = []
            for profile in profiles:
                emails.append(profile.user.email)

            subject = "مقاله جدید"
            message = f"""
            مقاله جدیدی در سایت
            ihosseinu.ir
            منتشر شده است.

            '{instance.title}'
            
            میتوانید از طریق لینک زیر مقاله را مشاهده کنید:

            https://www.ihosseinu.ir{reverse('article-detail', kwargs={'pk':instance.id})}

             """
            from_email = "ihosseinu.ir"
            datatuple = (subject, message, from_email, emails)
            send_mass_mail((datatuple,))
