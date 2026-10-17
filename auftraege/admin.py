from django.contrib import admin
from auftraege.models import Auftrag

# Register your models here.

class AuftragAdmin(admin.ModelAdmin):
    list_display = ('kunde', 'kunden_nummer', 'status', 'erstellt_am')
    list_filter = ('status', 'erstellt_am')
    search_fields = ('kunde', 'kunden_nummer')

admin.site.register(Auftrag, AuftragAdmin)
