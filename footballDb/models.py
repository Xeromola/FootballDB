from django.db import models

# Create your models here.
class player(models.Model):
    FOOTBALL_POSITIONS = [
        ('CF', 'Center-Forward'),
        ('SS', 'Second-Striker'),
        ('LWF', 'Left-Winger'),
        ('RWF', 'Right-Winger')
    ]
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    pos = models.CharField(max_length=3, choices=FOOTBALL_POSITIONS)
    nationality = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def which_position(self):
        return self.pos    