# Generated by Django 5.1.2 on 2024-10-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0003_alter_product_num_of_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
