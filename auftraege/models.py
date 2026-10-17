from django.db import models


class Status(models.TextChoices):
    OFFEN = 'offen', 'Offen'
    IN_ARBEIT = 'in_arbeit', 'In Arbeit'
    ERLEDIGT = 'erledigt', 'Erledigt' 



class Auftrag(models.Model):
    kunde = models.CharField(max_length=200)
    kunden_nummer = models.CharField(max_length=20)
    beschreibung = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OFFEN,
    )
    erstellt_am = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-erstellt_am"]


    def __str__(self):
        return f"{self.kunde} - {self.get_status_display()}"


