# Generated by Django 2.2 on 2019-04-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190410_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experince',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillone', models.CharField(max_length=100)),
                ('skilltwo', models.CharField(max_length=100)),
                ('skillthree', models.CharField(max_length=100)),
                ('skillfour', models.CharField(max_length=100)),
                ('skillfive', models.CharField(max_length=100)),
                ('skillsix', models.CharField(max_length=100)),
                ('skillseven', models.CharField(max_length=100)),
                ('skilleight', models.CharField(max_length=100)),
                ('skillnine', models.CharField(max_length=100)),
                ('skillten', models.CharField(max_length=100)),
                ('skilleleven', models.CharField(max_length=100)),
                ('skilltwelve', models.CharField(max_length=100)),
            ],
        ),
    ]