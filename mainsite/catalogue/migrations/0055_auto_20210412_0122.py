# Generated by Django 3.1.7 on 2021-04-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0054_auto_20210412_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application_records',
            old_name='color',
            new_name='color_code',
        ),
        migrations.AddField(
            model_name='application_records',
            name='color_ch',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='application_records',
            name='status',
            field=models.CharField(choices=[('application_submited', '申請已提交，但平台尚未收到賣家寄來的商品'), ('package_received', '平台已收到賣家寄來的商品，審查中'), ('on_selling', '已上架')], default='default', max_length=100),
        ),
    ]
