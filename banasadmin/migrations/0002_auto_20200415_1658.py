# Generated by Django 3.0.4 on 2020-04-15 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banasadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pwd',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='pwd1',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
