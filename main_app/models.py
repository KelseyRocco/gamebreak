from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#CONSTANTS
GENRES=(
    ('A', 'Adventure'),
    ('F', 'Fighting'),
    ('I', 'Indie'),
    ('R', 'Racing'),
    ('S', 'Sport'),
    ('T', 'Tactical')
)

MODES =(
    ('M', 'Multiplayer'),
    ('S', 'Single player'),
    ('C', 'Co-operative'),
    ('B', 'Battle Royale')
)

PLAYERS = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4+', 'Four')
)

# Game model
class Game(models.Model):
    title = models.CharField(max_length=100)
    date = models.IntegerField()
    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        default=GENRES[0][0]
    )
    mode = models.CharField(
        max_length=1,
        choices=MODES,
        default=MODES[0][0]
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):        
        return reverse('games_detail', kwargs={'pk': self.id})

#Systems model
class System(models.Model):
    name = models.CharField(max_length =250)
    date = models.IntegerField()
    platform = models.CharField(max_length=250)
    people = models.IntegerField(
        # choices=PLAYERS,
        # default=PLAYERS[0][1]
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):        
        return reverse('systems_detail', kwargs={'pk': self.id})
