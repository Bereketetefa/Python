# Generated by Django 2.2.4 on 2020-05-15 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloApp', '0003_auto_20200514_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.IntegerField(),
        ),
    ]