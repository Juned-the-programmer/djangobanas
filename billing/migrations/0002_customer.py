# Generated by Django 3.0.4 on 2020-04-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('route', models.CharField(max_length=100)),
            ],
        ),
    ]
