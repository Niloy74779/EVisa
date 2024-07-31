# Generated by Django 4.2.14 on 2024-07-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visaprocess', '0006_alter_visastatus_traking_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visaapplication',
            old_name='health_information',
            new_name='travel_insurance',
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='visa_type',
            field=models.CharField(choices=[('Tourist', 'Tourist'), ('Business', 'Business'), ('Student', 'Student'), ('Work', 'Work'), ('Medical', 'Medical'), ('Family', 'Family')], max_length=20),
        ),
    ]
