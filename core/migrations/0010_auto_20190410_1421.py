# Generated by Django 2.2 on 2019-04-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, height_field=300, upload_to=''),
        ),
    ]
