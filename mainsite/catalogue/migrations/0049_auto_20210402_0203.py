# Generated by Django 3.1.7 on 2021-04-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0048_auto_20210402_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='options',
            field=models.ManyToManyField(to='catalogue.OnehalfOption'),
        ),
    ]