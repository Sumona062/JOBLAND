# Generated by Django 3.1.2 on 2020-12-05 04:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
