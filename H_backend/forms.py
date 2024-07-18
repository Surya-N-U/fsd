from django import forms
from .models import Plant, NewPlant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'image', 'description', 'scientific_name', 'family', 'genus', 'species', 'location', 'collection_date']

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class NewPlantForm(forms.ModelForm):
    class Meta:
        model = NewPlant
        fields = ['name', 'image', 'description', 'family', 'type']

class NewImageUploadForm(forms.Form):
    image = forms.ImageField()