# Generated by Django 5.1.2 on 2024-12-01 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AquaFlowApp', '0002_remove_area_model_authority_remove_area_model_staff_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application_model',
            old_name='Adhar_photo',
            new_name='Aadhaar_photo',
        ),
        migrations.RemoveField(
            model_name='complaints_model',
            name='Reply',
        ),
    ]
