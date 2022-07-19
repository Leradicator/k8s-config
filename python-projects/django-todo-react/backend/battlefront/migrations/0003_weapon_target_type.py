# Generated by Django 4.0.6 on 2022-07-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battlefront', '0002_alter_weapon_life_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='target_type',
            field=models.CharField(choices=[('H', 'Heal Single Target'), ('A', 'Attack Single Target'), ('G', 'Attack Group'), ('D', 'Defend Single Target'), ('W', 'Defend Group')], default='A', max_length=1),
            preserve_default=False,
        ),
    ]