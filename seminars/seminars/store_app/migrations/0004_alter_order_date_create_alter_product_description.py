# Generated by Django 4.2.4 on 2023-08-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_rename_product_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_create',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
