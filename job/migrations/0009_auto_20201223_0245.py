# Generated by Django 3.1.2 on 2020-12-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_filledjobmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filledjobmodel',
            name='feedback',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]