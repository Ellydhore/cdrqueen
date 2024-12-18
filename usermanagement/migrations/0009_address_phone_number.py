# Generated by Django 5.1.1 on 2024-11-16 02:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0008_alter_address_address_label_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format: '+639XXXXXXXXX' or '09XXXXXXXXX'. Exactly 11 digits after the country code or leading zero.", regex='^(?:\\+63|0)\\d{10}$')]),
        ),
    ]
