from django.contrib import admin
from .models import ElectronicWasteType, EWasteCollection
from .forms import EWasteCollectionForm

@admin.register(ElectronicWasteType)
class ElectronicWasteTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(EWasteCollection)
class EWasteCollectionAdmin(admin.ModelAdmin):
    form = EWasteCollectionForm  # Use the custom form for this model
    list_display = ('waste_type', 'quantity', 'location','visible', 'date_submitted')
    list_filter = ('visible',)
    search_fields = ('waste_type', 'location')
