from django.db import models
from .validators import validate_factor, validate_life_factor, validate_attack_mod, validate_endurance_mod, validate_life_mod, validate_defense_mod
from .validators import validate_attack_capacity, validate_endurance_capacity, validate_life_capacity, validate_defense_capacity

# Create your models here.

class Weapon(models.Model):
    SELECT_TARGET = (
        ('H', 'Heal Single Target'),
        ('A', 'Attack Single Target'),
        ('G', 'Attack Group'),
        ('D', 'Defend Single Target'),
        ('W', 'Defend Group'),
    )
    
    name = models.CharField(max_length=100,
        unique = True)
    attack_factor = models.FloatField(default=1.0,
        help_text="attack multiplier, between 0.5 and 1.5",
        validators=[validate_factor])
    attack_modifier = models.IntegerField(default=3,
        help_text="attack adder, between 0 and 6",
        validators=[validate_attack_mod])
    endurance_factor = models.FloatField(default=1.0,
        help_text="endurance multiplier, between 0.5 and 1.5",
        validators=[validate_factor])
    endurance_modifier = models.IntegerField(default=6,
        help_text="endurance adder, between 3 and 9",
        validators=[validate_endurance_mod])
    life_factor = models.FloatField(default=0.5,
        help_text="life multiplier, between 0.0 and 1.0",
        validators=[validate_life_factor])
    life_modifier = models.IntegerField(default=0,
        help_text="life adder, between -3 and 3",
        validators=[validate_life_mod])
    defense_factor = models.FloatField(default=1.0,
        help_text="defense multiplier, between 0.5 and 1.5",
        validators=[validate_factor])
    defense_modifier = models.IntegerField(default=0,
        help_text="defense adder, between -3 and 3",
        validators=[validate_defense_mod])
    target_type = models.CharField(max_length=1, choices=SELECT_TARGET,
        help_text="one of 'H', 'A', 'G', 'D', 'W', see source code"
    )
    
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100,
        unique = True)
    
    def __str__(self):
        return self.name

class Fighter(models.Model):
    name = models.CharField(max_length=100,
        unique = True)
    attack_capacity = models.IntegerField(default=6,
        help_text="attack characteristic, between 0 and 12",
        validators=[validate_attack_capacity])
    endurance_capacity = models.IntegerField(default=6,
        help_text="endurance multiplier, between 0 and 12",
        validators=[validate_endurance_capacity])
    life_capactity = models.IntegerField(default=18,
        help_text="life multiplier, between 12 and 24",
        validators=[validate_life_capacity])
    defense_capacity = models.IntegerField(default=3,
        help_text="defense multiplier, between 0 and 6",
        validators=[validate_defense_capacity])
    weapon = models.ForeignKey(Weapon, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group,
        on_delete=models.DO_NOTHING, null=True, blank=True)
    single_target = models.ForeignKey('self',
        verbose_name='attacked single target',
        on_delete=models.DO_NOTHING, null=True, blank=True)
    group_target = models.ForeignKey(Group,
        related_name = 'group_target',
        verbose_name='attacked group target',
        on_delete=models.DO_NOTHING, null=True, blank=True)
    
    def __str__(self):
        return self.name
