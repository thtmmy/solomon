from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import *

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(customer_profile, sender=User)

def deposit(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='deposit')
        instance.groups.add(group)
        Deposit.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(deposit, sender=User)

def wallet(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='wallet')
        instance.groups.add(group)
        Wallet.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(wallet, sender=User)


def alert(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='alert')
        instance.groups.add(group)
        Alert.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(alert, sender=User)


def alert1(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='alert1')
        instance.groups.add(group)
        Alert1.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(alert1, sender=User)

def alert2(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='alert2')
        instance.groups.add(group)
        Alert2.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(alert2, sender=User)

def pin(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='pin')
        instance.groups.add(group)
        Pin.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(pin, sender=User)


def transaction(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='transaction')
        instance.groups.add(group)
        Transaction.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(transaction, sender=User)