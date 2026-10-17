from django.shortcuts import render
from .models import Auftrag

def auftrag_liste(request):
    auftraege = Auftrag.objects.all()
    return render(request, "auftraege/auftrag_liste.html", {"auftraege": auftraege})

