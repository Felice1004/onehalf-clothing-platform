# Generated by Django 3.1.7 on 2021-04-20 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0065_auto_20210421_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 1, 26, 40, 841009), verbose_name='儲存日期'),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, verbose_name='最後修改日期'),
        ),
    ]