from django.shortcuts import render
from .models import Technics

def technice_view(request):
    # print(request.method)
    data = Technics.objects.all()
    return render(request, 'APP/index.html', {'data': data})
