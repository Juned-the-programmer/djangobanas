# Generated by Django 3.2.4 on 2021-06-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banasadmin', '0014_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]