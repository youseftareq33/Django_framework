from django.shortcuts import render, redirect
from .models import Vehicle, Car, Bus

#------ vehicle views:

# create:
def create_vehicle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        
        vehicle = Vehicle(name=name, model=model, year=year, price=price)
        vehicle.save()
        return redirect('list_vehicles')

    return render(request, 'create_vehicle.html')

# list:
def list_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'list_vehicles.html', {'vehicles': vehicles})

# delete:
def delete_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        vehicle.delete()
    except Vehicle.DoesNotExist:
        pass  

    return redirect('list_vehicles')

# update:
def update_vehicle(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)

        if request.method == 'POST':
            name = request.POST.get('name')
            model = request.POST.get('model')
            year = request.POST.get('year')
            price = request.POST.get('price')

            vehicle.name = name
            vehicle.model = model
            vehicle.year = year
            vehicle.price = price
            vehicle.save()

            return redirect('list_vehicles')

    except Vehicle.DoesNotExist:
        vehicle = None  

    return render(request, 'update_vehicle.html', {'vehicle': vehicle})

#----------------------------------------------------------------------

#------ car views:

# create:
def create_car(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        color = request.POST.get('color')
        
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            vehicle = None  

        if vehicle:
            car = Car(vehicle=vehicle, color=color)
            car.save()
            return redirect('list_cars')

    vehicles = Vehicle.objects.all()
    return render(request, 'create_car.html', {'vehicles': vehicles})

# list:
def list_cars(request):
    cars = Car.objects.all()
    return render(request, 'list_cars.html', {'cars': cars})

# delete:
def delete_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        car.delete()
    except Car.DoesNotExist:
        pass  

    return redirect('list_cars')

# update:
def update_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)

        if request.method == 'POST':
            color = request.POST.get('color')

            car.color = color
            car.save()

            return redirect('list_cars')

    except Car.DoesNotExist:
        car = None  

    return render(request, 'update_car.html', {'car': car})

#----------------------------------------------------------------------

#------ bus views:

# create:
def create_bus(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        passenger_capacity = request.POST.get('passenger_capacity')
        
        try:
            vehicle = Vehicle.objects.get(pk=vehicle_id)
        except Vehicle.DoesNotExist:
            vehicle = None  

        if vehicle:
            bus = Bus(vehicle=vehicle, passenger_capacity=passenger_capacity)
            bus.save()
            return redirect('list_buses')

    vehicles = Vehicle.objects.all()
    return render(request, 'create_bus.html', {'vehicles': vehicles})

#list:
def list_buses(request):
    buses = Bus.objects.all()
    return render(request, 'list_buses.html', {'buses': buses})

# delete:
def delete_bus(request, bus_id):
    try:
        bus = Bus.objects.get(pk=bus_id)
        bus.delete()
    except Bus.DoesNotExist:
        pass  

    return redirect('list_buses')

# update:
def update_bus(request, bus_id):
    try:
        bus = Bus.objects.get(pk=bus_id)

        if request.method == 'POST':
            passenger_capacity = request.POST.get('passenger_capacity')

            bus.passenger_capacity = passenger_capacity
            bus.save()

            return redirect('list_buses')

    except Bus.DoesNotExist:
        bus = None  

    return render(request, 'update_bus.html', {'bus': bus})