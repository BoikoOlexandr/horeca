# Generated by Django 3.2.9 on 2021-12-17 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('easytrade', '0010_remove_goods_goods_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='easytrade.goodtypes'),
        ),
    ]
