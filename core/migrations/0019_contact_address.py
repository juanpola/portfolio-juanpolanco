# Generated by Django 2.2 on 2019-04-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20190411_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default='address', max_length=100),
        ),
    ]
