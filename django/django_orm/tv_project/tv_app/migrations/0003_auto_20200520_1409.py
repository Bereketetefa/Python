# Generated by Django 2.2.4 on 2020-05-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0002_auto_20200520_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='Release',
            field=models.DateField(max_length=225),
        ),
    ]