# Generated by Django 3.1.7 on 2021-04-20 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0061_auto_20210421_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='儲存日期'),
        ),
    ]
