# Generated by Django 3.2.4 on 2021-07-09 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0010_auto_20210709_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activebountysubmission',
            name='active',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bounty.activebounty'),
        ),
    ]
