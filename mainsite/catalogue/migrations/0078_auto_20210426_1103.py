# Generated by Django 3.1.7 on 2021-04-26 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0077_auto_20210421_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 26, 11, 3, 34, 737468), verbose_name='儲存日期'),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='instock_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 26, 11, 3, 34, 737468), verbose_name='上架日期'),
        ),
    ]
