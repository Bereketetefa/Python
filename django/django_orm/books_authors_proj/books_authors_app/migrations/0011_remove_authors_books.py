# Generated by Django 2.2.4 on 2020-05-18 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0010_authors_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='books',
        ),
    ]