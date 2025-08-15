from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    search = request.GET.get('search')

    if not search:
        cars = Car.objects.all()
    else:
        cars = Car.objects.filter(model__icontains=search)

    return render(
        request,
        'cars.html',
        {'cars': cars}
        )