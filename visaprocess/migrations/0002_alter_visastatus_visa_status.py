# Generated by Django 4.2.15 on 2024-09-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visaprocess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visastatus',
            name='visa_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Schedule', 'Schedule'), ('PoliceVerification', 'PoliceVerification'), ('AdminApprove', 'AdminApprove')], default='Pending', max_length=100),
        ),
    ]
