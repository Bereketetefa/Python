# Generated by Django 2.2.4 on 2020-05-17 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0009_auto_20200516_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='ninja',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
