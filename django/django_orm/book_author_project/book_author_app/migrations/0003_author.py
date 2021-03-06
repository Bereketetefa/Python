# Generated by Django 2.2.4 on 2020-05-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_author_app', '0002_auto_20200518_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('update', models.ManyToManyField(related_name='author', to='book_author_app.Book')),
            ],
        ),
    ]
