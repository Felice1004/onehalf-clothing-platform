# Generated by Django 3.1.7 on 2021-04-27 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0078_auto_20210426_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 23, 9, 23, 483500), verbose_name='儲存日期'),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='instock_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 23, 9, 23, 483500), verbose_name='上架日期'),
        ),
    ]
