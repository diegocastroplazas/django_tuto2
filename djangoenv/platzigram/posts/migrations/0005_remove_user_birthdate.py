# Generated by Django 2.1 on 2018-09-17 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_user_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
    ]