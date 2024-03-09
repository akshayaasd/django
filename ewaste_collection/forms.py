# forms.py

from django import forms
from .models import EWasteCollection, ElectronicWasteType

class EWasteCollectionForm(forms.ModelForm):
    waste_type = forms.ModelMultipleChoiceField(queryset=ElectronicWasteType.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = EWasteCollection
        fields = ['waste_image', 'waste_type', 'quantity','location']
