# Generated by Django 3.1.7 on 2021-04-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0031_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizeName', models.CharField(max_length=10)),
            ],
        ),
    ]
