# Generated by Django 4.0.5 on 2022-06-17 19:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Games', '0008_rename_siteuser_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='SiteUser',
        ),
    ]