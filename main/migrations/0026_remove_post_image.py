# Generated by Django 3.0 on 2020-07-21 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]