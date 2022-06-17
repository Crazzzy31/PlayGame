# Generated by Django 4.0.4 on 2022-06-14 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0006_alter_siteuser_roleid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRestrictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='CurrencyId',
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
        migrations.AlterField(
            model_name='game',
            name='AgeRestriction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ages', to='Games.agerestrictions'),
        ),
    ]
