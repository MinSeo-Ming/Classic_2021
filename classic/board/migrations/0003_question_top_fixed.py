# Generated by Django 3.2.5 on 2021-08-06 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20210805_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='top_fixed',
            field=models.BooleanField(default=False, verbose_name='상단고정'),
        ),
    ]
