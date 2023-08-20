from django.shortcuts import render
from .models import City

# Create your views here.
def city_view(request):
    obj=City.objects.all()
    for i in obj:
        context={
             'object':obj
        }
    return render(request,"Cities/detail.html",context)