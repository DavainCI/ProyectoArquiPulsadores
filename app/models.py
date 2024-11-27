from django.db import models

class Score(models.Model):
    player_name = models.CharField(max_length=50)  # Nombre del jugador
    score = models.IntegerField()                 # Puntuación
    date = models.DateTimeField(auto_now_add=True)  # Fecha automática

    def __str__(self):
        return f"{self.player_name} - {self.score}"
