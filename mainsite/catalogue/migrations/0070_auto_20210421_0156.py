# Generated by Django 3.1.7 on 2021-04-21 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0069_auto_20210421_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application_records',
            name='selling_date',
        ),
        migrations.AddField(
            model_name='application_records',
            name='instock_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 1, 56, 10, 748145), verbose_name='最後修改日期'),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 1, 56, 10, 748145), verbose_name='儲存日期'),
        ),
    ]
