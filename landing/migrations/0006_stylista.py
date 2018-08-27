# Generated by Django 2.1 on 2018-08-23 05:11

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import landing.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landing', '0005_auto_20180822_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stylista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('stylist_type', models.CharField(blank=True, choices=[('BARBER', 'Barber'), ('HAIR_STYLIST', 'Hair Stylist'), ('MAKEUP', 'Makeup Artist'), ('MUAH', 'Make Up And Hair'), ('NAILS', 'Nail Technician'), ('CLIENT', 'Client')], max_length=25)),
                ('about_me', models.TextField(blank=True)),
                ('business_name', models.CharField(blank=True, max_length=20)),
                ('services', django.contrib.postgres.fields.jsonb.JSONField()),
                ('address', models.CharField(blank=True, max_length=50)),
                ('business_address', models.CharField(blank=True, max_length=50)),
                ('zip_code', models.CharField(blank=True, max_length=8)),
                ('business_zip_code', models.CharField(blank=True, max_length=8)),
                ('city', models.CharField(blank=True, max_length=15)),
                ('business_city', models.CharField(blank=True, max_length=25)),
                ('country', models.CharField(blank=True, max_length=15)),
                ('business_country', models.CharField(blank=True, max_length=25)),
                ('business_location', models.CharField(blank=True, max_length=25)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?[1-9]\\d{1,14}$')])),
                ('business_phone_number', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?[1-9]\\d{1,14}$')])),
                ('store_front', models.ImageField(default='/user/storefront/default-storefront.jpg', upload_to=landing.models.Stylista.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]