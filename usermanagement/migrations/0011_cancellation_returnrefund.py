# Generated by Django 5.1.1 on 2024-11-28 08:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0010_alter_address_address_label_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancellation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('price', 'Found a better price elsewhere'), ('delay', 'Order delayed too long'), ('mind_change', 'Changed my mind about the purchase'), ('expectation', 'Product was not as expected'), ('mistake', 'Placed the order by mistake')], max_length=50)),
                ('cancel_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('denied', 'Denied')], default='pending', max_length=20)),
                ('canceled_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancellations', to='usermanagement.order')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnRefund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('damaged', 'Damaged product'), ('wrong_item', 'Received the wrong item'), ('quality', 'Product quality issue'), ('change_mind', 'Changed my mind'), ('other', 'Other')], max_length=50)),
                ('additional_details', models.TextField(blank=True, null=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('return_condition', models.CharField(choices=[('new', 'Unopened/New'), ('used', 'Used'), ('damaged', 'Damaged')], default='new', max_length=20)),
                ('refund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied'), ('refunded', 'Refunded')], default='pending', max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='returns', to='usermanagement.order')),
                ('processed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
