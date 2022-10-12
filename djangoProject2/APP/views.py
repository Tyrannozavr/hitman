from django.shortcuts import render
from .models import Technics

def technice_view(request):
    if request.method == 'POST':
        # print('post', request.POST)
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        print(age)
        print(name)
    if request.method == 'GET':
        print('get', request.GET)
    data = Technics.objects.all()
    return render(request, 'APP/index.html', {'data': data})
