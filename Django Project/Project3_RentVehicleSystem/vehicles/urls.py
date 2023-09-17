from django.urls import path
from . import views

urlpatterns = [
    # Vehicle URLs
    path('vehicles/create/', views.create_vehicle, name='create_vehicle'),
    path('vehicles/', views.list_vehicles, name='list_vehicles'),
    path('vehicles/<int:vehicle_id>/update/', views.update_vehicle, name='update_vehicle'),
    path('vehicles/<int:vehicle_id>/delete/', views.delete_vehicle, name='delete_vehicle'),
    
    # Car URLs
    path('cars/create/', views.create_car, name='create_car'),
    path('cars/', views.list_cars, name='list_cars'),
    path('cars/<int:car_id>/update/', views.update_car, name='update_car'),
    path('cars/<int:car_id>/delete/', views.delete_car, name='delete_car'),
    
    # Bus URLs
    path('buses/create/', views.create_bus, name='create_bus'),
    path('buses/', views.list_buses, name='list_buses'),
    path('buses/<int:bus_id>/update/', views.update_bus, name='update_bus'),
    path('buses/<int:bus_id>/delete/', views.delete_bus, name='delete_bus'),
]
