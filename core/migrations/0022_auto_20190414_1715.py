# Generated by Django 2.2 on 2019-04-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20190414_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
