# Generated by Django 5.1.6 on 2025-03-12 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_nutritionassessment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutritionassessment',
            old_name='dietary_preference',
            new_name='dietaryPreference',
        ),
        migrations.RenameField(
            model_name='nutritionassessment',
            old_name='food_frequency',
            new_name='foodFrequency',
        ),
        migrations.RenameField(
            model_name='nutritionassessment',
            old_name='medical_conditions',
            new_name='medicalConditions',
        ),
        migrations.RenameField(
            model_name='nutritionassessment',
            old_name='water_intake',
            new_name='waterIntake',
        ),
    ]
