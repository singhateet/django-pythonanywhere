# Generated by Django 4.1.7 on 2023-02-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no image', upload_to='images/'),
        ),
    ]
