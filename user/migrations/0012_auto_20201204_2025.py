# Generated by Django 3.1.2 on 2020-12-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20201202_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperiencemodel',
            name='job_type',
            field=models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Intern', 'Intern')], max_length=30, null=True),
        ),
    ]
