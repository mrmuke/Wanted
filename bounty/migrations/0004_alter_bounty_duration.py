# Generated by Django 3.2.4 on 2021-06-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0003_bounty_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='duration',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
