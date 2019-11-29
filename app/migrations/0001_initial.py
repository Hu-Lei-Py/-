# Generated by Django 2.2.3 on 2019-11-12 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='good_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='商品类目')),
                ('type_pic', models.CharField(max_length=100, verbose_name='图片链接')),
            ],
        ),
        migrations.CreateModel(
            name='good_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='商品名称')),
                ('image', models.CharField(max_length=100, verbose_name='商品图片路径')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='商品价格')),
                ('good_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.good_type', verbose_name='关联类别')),
            ],
        ),
    ]
