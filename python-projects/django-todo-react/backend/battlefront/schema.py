import graphene
from graphene_django import DjangoObjectType

from .models import Weapon, Group, Fighter

class WeaponType(DjangoObjectType):
    class Meta:
        model = Weapon
        fields = ('id', 'name', 'target_type')

class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = ('id', 'name')

class FighterType(DjangoObjectType):
    class Meta:
        model = Fighter
        fields = ('id', 'name', 'weapon', 'group', 'single_target', 'group_target')

class Query(graphene.ObjectType):
    all_weapons = graphene.List(WeaponType)
    all_groups = graphene.List(GroupType)
    all_fighters = graphene.List(FighterType)
    fighter_by_name = graphene.Field(FighterType, name=graphene.String(required=True))
    fighter_by_weapon = graphene.List(FighterType, weapon=graphene.String(required=True))
    
    def resolve_all_weapons(root, info):
        return Weapon.objects.all()
    
    def resolve_all_groups(root, info):
        return Group.objects.all()
    
    def resolve_all_fighters(root, info):
        return Fighter.objects.all()
    
    def resolve_fighter_by_name(root, info, name):
        try:
            return Fighter.objects.get(name=name)
        except Fighter.DoesNotExist:
            return None
    
    def resolve_fighter_by_weapon(root, info, weapon):
        try:
            weapon = Weapon.objects.filter(name=weapon)
            return Fighter.objects.filter(weapon__in=weapon)
        except Fighter.DoesNotExist:
            return None
        except Weapon.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
