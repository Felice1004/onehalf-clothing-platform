# Generated by Django 3.1.7 on 2021-04-20 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0063_auto_20210421_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateField(default=datetime.date(2021, 4, 21), verbose_name='儲存日期'),
        ),
    ]
