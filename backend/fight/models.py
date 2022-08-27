from authentication.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Fight(models.Model):
    choice = [
        ('голова', 'голова'),
        ('туловище', 'туловище'),
        ('левая рука', 'левая рука'),
        ('правая рука', 'правая рука'),
        ('левая нога', 'левая нога'),
        ('правая нога', 'правая нога'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attack = ArrayField(
        models.CharField(max_length=40, choices=choice), size=3
    )
    defend = ArrayField(
        models.CharField(max_length=40, choices=choice), size=3
    )
    finished = models.BooleanField(default=False)

class Statistic(models.Model):
    num_round = models.AutoField(primary_key=True)
    first_player = models.OneToOneField(Fight, on_delete=models.CASCADE, related_name='first')
    second_player = models.OneToOneField(Fight, on_delete=models.CASCADE, related_name='second')
    first_player_score = models.IntegerField(default=0)
    second_player_score = models.IntegerField(default=0)

