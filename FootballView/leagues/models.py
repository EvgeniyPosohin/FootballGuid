from django.db import models


class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    logo = models.URLField(blank=True, null=True)
    external_id = models.CharField(max_length=50, blank=True, null=True)  # ID provider

    def __str__(self):
        return f"{self.name} ({self.country})"

class Season(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="seasons")
    year = models.CharField(max_length=20)  # for example, "2023/24"
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.league.name} {self.year}"