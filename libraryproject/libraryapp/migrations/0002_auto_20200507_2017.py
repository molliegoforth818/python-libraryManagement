# Generated by Django 3.0.6 on 2020-05-07 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ibsn',
            new_name='isbn',
        ),
    ]