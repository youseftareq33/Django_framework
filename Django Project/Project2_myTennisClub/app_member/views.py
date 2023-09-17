from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import Member

class JSONDataView(View):
    def get(self, request):
        data = {'message': 'Hello, world!'}
        return JsonResponse(data)
    
def message(request):
    return HttpResponse("Hello World")

def create_member(request):
    if request.method == 'POST':        
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        
        member = Member(firstname=firstname, lastname=lastname)
        member.save()

        return redirect('success_page')

    return render(request, 'create_member.html')



def list_members(request):
    members = Member.objects.all()
    return render(request, 'list_members.html', {'members': members})



def update_member(request, member_id):
    try:
        member = Member.objects.get(pk=member_id)

        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')

            member.firstname = firstname
            member.lastname = lastname
            member.save()

            return redirect('success_page')

    except Member.DoesNotExist:
        pass

    return render(request, 'update_member.html', {'member': member})