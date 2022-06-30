from django.db import models
from authentication.models import User
from django.contrib.postgres.fields import ArrayField

class Fight(models.Model):
    choice = [
        ('1', 'Голова'),
        ('2', 'Туловище'),
        ('3', 'Левая рука'),
        ('4', 'Правая рука'),
        ('5', 'Левая нога'),
        ('6', 'Правая нога'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attack = ArrayField(
        models.CharField(max_length=40, choices=choice), size=3
    )
    defend = ArrayField(
        models.CharField(max_length=40, choices=choice), size=3
    )
