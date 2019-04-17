# Generated by Django 2.2 on 2019-04-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190410_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('image', models.ImageField(height_field=300, upload_to='')),
                ('url', models.URLField(blank=True, max_length=50)),
            ],
        ),
    ]