# Generated by Django 4.0.4 on 2022-06-13 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0004_rename_user_siteuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='RoleId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Games.role'),
        ),
    ]
