# Generated by Django 3.1.2 on 2020-12-08 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_applicantprofilemodel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicantprofilemodel',
            name='slug',
        ),
    ]
