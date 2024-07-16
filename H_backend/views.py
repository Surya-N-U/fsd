from django.shortcuts import render, redirect
from .models import Plant
from .forms import PlantForm
from django.db.models import Count
from .forms import ImageUploadForm
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np


def upload_image(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('H_backend:upload_image')
    else:
        form = PlantForm()
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

def analytics(request):
    # Count the number of plants by family
    family_counts = Plant.objects.values('family').annotate(total=Count('family')).order_by('-total')

    context = {
        'family_counts': family_counts,
    }

    return render(request, 'plants/analytics.html', context)

model = MobileNetV2(weights='imagenet')

def scan_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the uploaded image
            image = form.cleaned_data['image']
            image_path = 'media/' + image.name
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            
            # Preprocess the image for the model
            img = load_img(image_path, target_size=(224, 224))
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # Perform inference
            predictions = model.predict(img_array)
            decoded_predictions = decode_predictions(predictions, top=3)[0]

            context = {
                'form': form,
                'image_url': image_path,
                'predictions': decoded_predictions,
            }
            return render(request, 'plants/scan_results.html', context)
    else:
        form = ImageUploadForm()
    return render(request, 'plants/scan_image.html', {'form': form})