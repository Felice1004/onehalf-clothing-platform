# Generated by Django 3.1.7 on 2021-04-20 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0062_auto_20210421_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateField(default=datetime.date.today, verbose_name='儲存日期'),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='mod_date',
            field=models.DateField(auto_now=True, verbose_name='最後修改日期'),
        ),
    ]