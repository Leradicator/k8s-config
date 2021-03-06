# Generated by Django 4.0.6 on 2022-07-19 08:19

import battlefront.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battlefront', '0003_weapon_target_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='life_factor',
            field=models.FloatField(default=0.5, help_text='life multiplier', validators=[battlefront.validators.validate_life_factor]),
        ),
    ]
