# Generated by Django 3.0.5 on 2020-05-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banasadmin', '0009_auto_20200502_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyentry',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
