from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'image', 'description', 'scientific_name', 'family', 'genus', 'species', 'location', 'collection_date']
