# Generated by Django 2.2 on 2019-04-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190410_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.CharField(blank=True, max_length=300)),
                ('two', models.CharField(blank=True, max_length=300)),
                ('three', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
