from django.shortcuts import render, redirect, get_object_or_404
from .models import Package
from .forms import TrackingForm
from .forms import PackageForm

def home(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            package = get_object_or_404(Package, tracking_id=tracking_id)
            return render(request, 'track.html', {'package': package})
    else:
        form = TrackingForm()
    return render(request, 'index.html', {'form': form})


def track(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            package = get_object_or_404(Package, tracking_id=tracking_id)
            return render(request, 'track.html', {'package': package})
    else:
        form = TrackingForm()
    return render(request, 'track.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request,'services.html')


def services_details(request):
    # return render(request, 'services-details.html')
    return render(request, 'service-details.html')


def add_package(request):
    tracking_id = None
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save()
            tracking_id = package.tracking_id
            # return redirect('about')  
            # # Redirect to a list view or detail view after saving
            return render(request, 'add_package.html', {'form': form, 'tracking_id': tracking_id})
    else:
        form = PackageForm()

    # return render(request, 'add_package.html', {'form': form})
    return render(request, 'add_package.html', {'form': form, 'tracking_id': tracking_id})