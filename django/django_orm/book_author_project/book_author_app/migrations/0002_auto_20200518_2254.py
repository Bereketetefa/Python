# Generated by Django 2.2.4 on 2020-05-19 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_author_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(max_length=225),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=225),
        ),
    ]