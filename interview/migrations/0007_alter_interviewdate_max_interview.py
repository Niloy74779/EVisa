# Generated by Django 4.2.14 on 2024-07-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_alter_interviewdate_max_interview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewdate',
            name='max_interview',
            field=models.IntegerField(default=3),
        ),
    ]
