# Generated by Django 5.1.1 on 2024-10-15 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0003_product_ave_ratings_product_num_of_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_url_1',
            field=models.URLField(default='https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM='),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_url_2',
            field=models.URLField(default='https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM='),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_url_3',
            field=models.URLField(default='https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM='),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_url_4',
            field=models.URLField(default='https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM='),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_url_5',
            field=models.URLField(default='https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM='),
        ),
    ]
