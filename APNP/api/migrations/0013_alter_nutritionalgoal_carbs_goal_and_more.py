# Generated by Django 5.1.6 on 2025-04-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_nutritionalgoal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='carbs_goal',
            field=models.CharField(default='0g', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='carbs_taken',
            field=models.CharField(default='0g', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='fat_goal',
            field=models.CharField(default='0g', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='fat_taken',
            field=models.CharField(default='0g', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='fiber_goal',
            field=models.CharField(default='0g', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='fiber_taken',
            field=models.CharField(default='0g', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='goal_calories',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='micro1_goal',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='micro1_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='micro2_goal',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='micro2_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='micro3_goal',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='micro3_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='protein_goal',
            field=models.CharField(default='0g', max_length=20),
        ),
        migrations.AlterField(
            model_name='nutritionalgoal',
            name='protein_taken',
            field=models.CharField(default='0g', max_length=20),
        ),
    ]
