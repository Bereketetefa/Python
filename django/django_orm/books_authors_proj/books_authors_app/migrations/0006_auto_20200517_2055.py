# Generated by Django 2.2.4 on 2020-05-18 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0005_authors_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authors',
            old_name='books',
            new_name='Books',
        ),
    ]