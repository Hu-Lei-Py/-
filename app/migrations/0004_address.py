# Generated by Django 2.2.3 on 2019-11-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191121_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40, verbose_name='地址')),
                ('user', models.CharField(max_length=50, verbose_name='用户')),
                ('phone', models.IntegerField(max_length=30, verbose_name='电话')),
            ],
        ),
    ]
