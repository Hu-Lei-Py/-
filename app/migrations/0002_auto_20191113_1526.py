# Generated by Django 2.2.3 on 2019-11-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good_info',
            name='title',
            field=models.CharField(max_length=150, verbose_name='商品名称'),
        ),
    ]
