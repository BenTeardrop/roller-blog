# Generated by Django 3.2.15 on 2022-08-26 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mynews', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='review',
            name='post',
        ),
    ]
