# Generated by Django 2.2.4 on 2020-05-16 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_ninjas_uploader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninjas',
            name='uploader',
        ),
    ]