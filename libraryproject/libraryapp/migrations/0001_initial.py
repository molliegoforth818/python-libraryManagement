# Generated by Django 3.0.6 on 2020-05-07 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'library',
                'verbose_name_plural': 'libraries',
            },
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='librarians', to='libraryapp.Library')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('ibsn', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('year_published', models.IntegerField()),
                ('publisher', models.CharField(max_length=50)),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Librarian')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Library')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
    ]
