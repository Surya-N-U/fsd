from django.shortcuts import render, redirect
from .models import Plant, NewPlant, Algae
from .forms import PlantForm, NewPlantForm, AlgaeForm
from django.db.models import Count
from .forms import ImageUploadForm
from django.contrib.auth.decorators import login_required
# from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# import numpy as np


def home(request):
    return render(request, 'index.html')


def algae(request):
    algae_items = NewPlant.objects.filter(type='Algae')
    return render(request, 'algae.html', {'algae_items': algae_items})


def gymnosperms(request):
    gymno_items = NewPlant.objects.filter(type='Gymnosperms')
    return render(request, 'gymnosperms.html', {'gymno_items': gymno_items})


def angiosperms(request):
    angio_items = NewPlant.objects.filter(type='Angiosperms')
    return render(request, 'angiosperms.html', {'angio_items': angio_items})


def pteridophytes(request):
    pteri_items = NewPlant.objects.filter(type='Pteridophytes')
    return render(request, 'pteridophytes.html', {'pteri_items': pteri_items})


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = AlgaeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('H_backend:upload_image')
    else:
        form = AlgaeForm()
    return render(request, 'plants/upload_image.html', {'form': form})


def search_images(request):
    query = request.GET.get('query')
    if query:
        results = Plant.objects.filter(

            family__icontains=query
        )
    else:
        results = Plant.objects.all()
    return render(request, 'plants/search_results.html', {'results': results})


@login_required
def analytics(request):
    # Count the number of plants by family
    family_counts = NewPlant.objects.values('family').annotate(
        total=Count('family')).order_by('-total')

    context = {
        'family_counts': family_counts,
    }

    return render(request, 'plants/analytics.html', context)
