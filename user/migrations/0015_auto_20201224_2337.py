# Generated by Django 3.1.2 on 2020-12-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_remove_applicantprofilemodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagemodel',
            name='proficiency',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Native', 'Native')], max_length=30, null=True),
        ),
    ]
