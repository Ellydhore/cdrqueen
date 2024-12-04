# Generated by Django 5.1.1 on 2024-11-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0007_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_label',
            field=models.CharField(choices=[('home', 'Home'), ('work', 'Work')], default='home', max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('default', 'Default'), ('pickup_address', 'Pickup Address'), ('return_address', 'Return Address')], default='default', max_length=15),
        ),
    ]