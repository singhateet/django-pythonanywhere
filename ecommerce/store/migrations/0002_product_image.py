# Generated by Django 4.1.7 on 2023-02-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='image', upload_to='images/'),
        ),
    ]
