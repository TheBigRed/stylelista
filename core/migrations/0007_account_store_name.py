# Generated by Django 2.0.4 on 2018-05-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180530_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='store_name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
