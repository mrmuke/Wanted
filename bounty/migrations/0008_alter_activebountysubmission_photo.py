# Generated by Django 3.2.4 on 2021-07-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0007_activebounty_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activebountysubmission',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='bounty_submission'),
        ),
    ]
