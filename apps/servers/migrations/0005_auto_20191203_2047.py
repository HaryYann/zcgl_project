# Generated by Django 2.2.3 on 2019-12-03 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_auto_20191203_2037'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServerHis',
        ),
        migrations.AlterField(
            model_name='server',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
