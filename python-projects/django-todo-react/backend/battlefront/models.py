from django.db import models
from .validators import validate_factor, validate_attack_mod, validate_endurance_mod, validate_life_mod, validate_defense_mod

# Create your models here.

class Weapon(models.Model):
    name = models.CharField(max_length=100,
        unique = True)
    attack_factor = models.FloatField(default=1.0,
        help_text="attack multiplier",
        validators=[validate_factor])
    attack_modifier = models.IntegerField(default=3,
        help_text="attack adder",
        validators=[validate_attack_mod])
    endurance_factor = models.FloatField(default=1.0,
        help_text="endurance multiplier",
        validators=[validate_factor])
    endurance_modifier = models.IntegerField(default=6,
        help_text="endurance adder",
        validators=[validate_endurance_mod])
    life_factor = models.FloatField(default=0.0,
        help_text="life multiplier",
        validators=[validate_factor])
    life_modifier = models.IntegerField(default=0,
        help_text="life adder",
        validators=[validate_life_mod])
    defense_factor = models.FloatField(default=1.0,
        help_text="defense multiplier",
        validators=[validate_factor])
    defense_modifier = models.IntegerField(default=3,
        help_text="defense adder",
        validators=[validate_defense_mod])
    
    def __str__(self):
        return self.name
