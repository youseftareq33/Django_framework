from django.urls import path
from .views import (UserRegistrationView,UserLoginView,ListItemsView,ListBestSellerItemsView,UpdateItemView,
                    AddItemView,DeleteItemView,AddItemToFavoritesView,RemoveItemFromFavoritesView,SendCreditCredentialsView)


urlpatterns = [
    path('register',UserRegistrationView.as_view()),
    path('login',UserLoginView.as_view()),
    path('ListItems',ListItemsView.as_view()),
    path('BestSellerItems',ListBestSellerItemsView.as_view()),
    path('UpdateItems',UpdateItemView.as_view()),
    path('AddItems',AddItemView.as_view()),
    path('DeleteItems',DeleteItemView.as_view()),
    path('AddItemstoFL',AddItemToFavoritesView.as_view()),
    path('RemoveItemsfromFL',RemoveItemFromFavoritesView.as_view()),
    path('SendCC',SendCreditCredentialsView.as_view()),
    
]
