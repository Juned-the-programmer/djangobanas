# Generated by Django 3.0.8 on 2020-08-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banasadmin', '0013_remove_customer_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
