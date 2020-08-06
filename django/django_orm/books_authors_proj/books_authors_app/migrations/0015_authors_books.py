# Generated by Django 2.2.4 on 2020-05-18 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0014_remove_authors_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='books',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='books_authors_app.books'),
        ),
    ]
