# Generated by Django 5.0.2 on 2024-02-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsapp', '0002_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
