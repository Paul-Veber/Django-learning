# Generated by Django 4.0.1 on 2022-01-18 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='body',
        ),
    ]