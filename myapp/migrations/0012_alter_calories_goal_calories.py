# Generated by Django 4.0.4 on 2023-06-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_calories_goal_calories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calories_goal',
            name='Calories',
            field=models.IntegerField(default=2000),
        ),
    ]