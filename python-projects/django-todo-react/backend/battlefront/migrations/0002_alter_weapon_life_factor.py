# Generated by Django 4.0.6 on 2022-07-19 08:00

import battlefront.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battlefront', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='life_factor',
            field=models.FloatField(default=1.0, help_text='life multiplier', validators=[battlefront.validators.validate_factor]),
        ),
    ]
