# Generated by Django 3.0.5 on 2020-05-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banasadmin', '0008_auto_20200502_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='pending_amount',
            field=models.IntegerField(),
        ),
    ]