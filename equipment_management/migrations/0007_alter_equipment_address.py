# Generated by Django 5.0.7 on 2024-08-19 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0006_alter_equipment_slug'),
        ('user_management', '0003_alter_address_address_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.address'),
        ),
    ]
