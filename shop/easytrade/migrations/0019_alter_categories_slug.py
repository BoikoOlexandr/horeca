# Generated by Django 3.2.9 on 2021-12-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easytrade', '0018_alter_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(),
        ),
    ]