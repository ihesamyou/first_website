# Generated by Django 3.2.7 on 2021-12-06 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]