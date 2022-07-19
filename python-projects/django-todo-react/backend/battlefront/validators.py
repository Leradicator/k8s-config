from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_factor(value):
    if (value < 0.5) or (value > 1.5):
        raise ValidationError(
            _('factor %(value)s is not between 0.5 and 1.5'),
            params={'value': value},
        )

def validate_life_factor(value):
    if (value < 0.0) or (value > 1.0):
        raise ValidationError(
            _('factor %(value)s is not between 0.0 and 1.0'),
            params={'value': value},
        )

def validate_attack_mod(value):
    if (value > 6) or (value < 0):
        raise ValidationError(
            _('modifier %(value)s is not between 0 and 6'),
            params={'value': value},
        )

def validate_endurance_mod(value):
    if (value > 9) or (value < 3):
        raise ValidationError(
            _('modifier %(value)s is not between 3 and 9'),
            params={'value': value},
        )

def validate_life_mod(value):
    if (value > 3) or (value < -3):
        raise ValidationError(
            _('modifier %(value)s is not between -3 and 3'),
            params={'value': value},
        )

def validate_defense_mod(value):
    if (value > 3) or (value < -3):
        raise ValidationError(
            _('modifier %(value)s is not between -3 and 3'),
            params={'value': value},
        )

def validate_attack_capacity(value):
    if (value > 12) or (value < 0):
        raise ValidationError(
            _('modifier %(value)s is not between 0 and 12'),
            params={'value': value},
        )

def validate_endurance_capacity(value):
    if (value > 12) or (value < 0):
        raise ValidationError(
            _('modifier %(value)s is not between 0 and 12'),
            params={'value': value},
        )

def validate_life_capacity(value):
    if (value > 24) or (value < 12):
        raise ValidationError(
            _('modifier %(value)s is not between 12 and 24'),
            params={'value': value},
        )

def validate_defense_capacity(value):
    if (value > 6) or (value < 0):
        raise ValidationError(
            _('modifier %(value)s is not between 0 and 6'),
            params={'value': value},
        )
