import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Weapon, Group, Fighter

class WeaponType(DjangoObjectType):
    class Meta:
        model = Weapon
        fields = ('id', 'name', 'target_type')

class WeaponNode(DjangoObjectType):
    class Meta:
        model = Weapon
        filter_fields = ['name', 'target_type']
        interfaces = (relay.Node, )

class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = ('id', 'name')

class GroupNode(DjangoObjectType):
    class Meta:
        model = Group
        filter_fields = ['name']
        interfaces = (relay.Node, )

class FighterType(DjangoObjectType):
    class Meta:
        model = Fighter
        fields = ('id', 'name', 'weapon', 'group', 'single_target', 'group_target')

class FighterNode(DjangoObjectType):
    class Meta:
        model = Fighter
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'weapon__name': ['exact'],
            'group__name': ['exact', 'icontains'],
            'single_target': ['exact'],
            'group_target': ['exact'],
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    weapon = relay.Node.Field(WeaponNode)
    all_weapons = DjangoFilterConnectionField(WeaponNode)
    group = relay.Node.Field(GroupNode)
    all_groups = DjangoFilterConnectionField(GroupNode)
    fighter = relay.Node.Field(FighterNode)
    all_fighters = DjangoFilterConnectionField(FighterNode)
    fighter_by_name = graphene.Field(FighterType, name=graphene.String(required=True))
    fighter_by_weapon = graphene.List(FighterType, weapon=graphene.String(required=True))
    
    #def resolve_all_weapons(root, info):
    #    return Weapon.objects.all()
    #
    #def resolve_all_groups(root, info):
    #    return Group.objects.all()
    #
    #def resolve_all_fighters(root, info):
    #    return Fighter.objects.all()
    
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
