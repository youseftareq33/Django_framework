from django.urls import path
from .views import JSONDataView,json_data_view


urlpatterns = [
    path('json/', JSONDataView.as_view(), name='json_data_cbv'),  # class based View URL
    path('json-fbv/', json_data_view, name='json_data_fbv'),      # function based View URL
]