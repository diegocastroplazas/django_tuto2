# Generated by Django 2.1.3 on 2018-11-15 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_user_birthdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
