# Generated by Django 2.2.4 on 2020-05-18 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0004_authors_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.books'),
        ),
    ]
