# Generated by Django 5.0.6 on 2024-07-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_contact_remove_restaurant_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
