from django.urls import path
from .views import JSONDataView, message

urlpatterns = [
    path('json-cbv/', JSONDataView.as_view(), name='json_data_cbv'),  # URL for class-based View
    path('message-fbv/', message, name='message-fbv'),  # URL for function-based View
]
