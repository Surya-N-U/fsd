from django import forms
from .models import Plant, NewPlant, Algae


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'image', 'description', 'scientific_name', 'family',
                  'genus', 'species', 'location', 'collection_date']


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class NewPlantForm(forms.ModelForm):
    class Meta:
        model = NewPlant
        fields = ['name', 'image', 'description', 'family', 'type']


class NewImageUploadForm(forms.Form):
    image = forms.ImageField()


class AlgaeForm(forms.ModelForm):
    class Meta:
        model = Algae
        fields = ['scientific_name', 'image', 'family',
                  'genus', 'species', 'location', 'collection_date', 'collected_by']


class AlgaeImageUploadForm(forms.Form):
    image = forms.ImageField()
