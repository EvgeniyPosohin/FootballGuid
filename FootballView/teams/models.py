from django.db import models
from FootballView.leagues.models import League


class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")
    logo = models.URLField(blank=True, null=True)
    external_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    full_name =  models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="players")
    avatar = models.URLField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    external_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
