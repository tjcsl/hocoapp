from django.db import models

from ..events.models import Event


class ScoreBoard(models.Model):

    """A ScoreBoard keeps track of an Event.
    It has a score field for all 4 classes"""

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    freshman_score = models.IntegerField(default=0)
    sophomore_score = models.IntegerField(default=0)
    junior_score = models.IntegerField(default=0)
    senior_score = models.IntegerField(default=0)

    @classmethod
    def create(
        cls,
        event: Event,
        freshman_score: int = 0,
        sophomore_score: int = 0,
        junior_score: int = 0,
        senior_score: int = 0,
    ):  # pylint: disable=too-many-arguments
        scoreboard = cls(
            event=event,
            freshman_score=freshman_score,
            sophomore_score=sophomore_score,
            junior_score=junior_score,
            senior_score=senior_score,
        )
        scoreboard.save()
        return scoreboard

    def __str__(self):
        return str(self.event)
