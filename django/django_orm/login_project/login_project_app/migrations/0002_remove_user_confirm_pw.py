# Generated by Django 2.2.4 on 2020-05-22 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_project_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_pw',
        ),
    ]