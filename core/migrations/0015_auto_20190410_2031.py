# Generated by Django 2.2 on 2019-04-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
