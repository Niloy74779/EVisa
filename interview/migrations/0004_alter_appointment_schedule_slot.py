# Generated by Django 4.2.15 on 2024-09-09 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_alter_admininterviewinfo_total_interview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='schedule_slot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='interview.scheduleslot'),
        ),
    ]
