# Generated by Django 3.2.9 on 2021-12-28 12:44

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('easytrade', '0016_remove_categories_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
    ]
