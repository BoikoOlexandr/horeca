# Generated by Django 3.2.9 on 2021-12-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easytrade', '0014_auto_20211228_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(),
        ),
    ]
