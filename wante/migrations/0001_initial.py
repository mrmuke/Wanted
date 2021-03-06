# Generated by Django 3.2.3 on 2021-06-22 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wante.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bounty', models.IntegerField()),
                ('collected', models.IntegerField(default=0)),
                ('who', models.CharField(max_length=1000)),
                ('what', models.CharField(max_length=1000)),
                ('where', models.CharField(max_length=1000)),
                ('why', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=wante.models.nameFile)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
