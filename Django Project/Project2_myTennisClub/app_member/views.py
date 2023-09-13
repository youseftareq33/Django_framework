from django.http import JsonResponse
from django.views import View

class JSONDataView(View):
    def get(self, request):
        data = {'message': 'Hello, world!'}
        return JsonResponse(data)
    
def json_data_view(request):
    data = {'message': 'Hello, world!'}
    return JsonResponse(data)