# Generated by Django 2.2.4 on 2020-05-18 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0008_auto_20200517_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='books',
        ),
    ]