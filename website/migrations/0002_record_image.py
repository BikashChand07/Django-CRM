# Generated by Django 5.1.5 on 2025-02-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='customer_images/'),
        ),
    ]
