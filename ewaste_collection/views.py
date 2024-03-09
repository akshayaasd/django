from django.shortcuts import render, redirect
from .forms import EWasteCollectionForm
from .models import EWasteCollection

def index(request):
    if request.method == 'POST':
        form = EWasteCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            ewaste = form.save(commit=False)  # Don't save immediately for custom visibility logic
            ewaste.visible = request.POST.get('visible', False) == 'on'  # Set visibility based on checkbox
            ewaste.save()  # Now save the instance with visibility
            return render(request, 'ewaste_collection_success.html')
    else:
        form = EWasteCollectionForm()
    return render(request, 'index.html', {'form': form})

def ewaste_collection_success(request):
    return render(request, 'ewaste_collection_success.html')

def show_ewaste(request):
    # Filter e-waste based on visibility preference (optional)
    visible_ewastes = EWasteCollection.objects.filter(visible=True)  # Default to visible

    # Optionally allow filtering by user preference
    user_preference = request.GET.get('visible', '')  # Get visibility preference from URL query string (if any)
    if user_preference.lower() == 'all':  # If user wants to see all e-waste
        visible_ewastes = EWasteCollection.objects.all()  # Show all

    context = {'ewastes': visible_ewastes}
    return render(request, 'show_ewaste.html', context)
