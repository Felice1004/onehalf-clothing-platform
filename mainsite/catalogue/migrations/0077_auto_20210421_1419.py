# Generated by Django 3.1.7 on 2021-04-21 14:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0076_auto_20210421_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_records',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 14, 19, 30, 164080), verbose_name='儲存日期'),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='instock_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 14, 19, 30, 165078), verbose_name='上架日期'),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.product'),
        ),
    ]