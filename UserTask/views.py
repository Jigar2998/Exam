from django.shortcuts import render
from django.http import request
from .models import user
# Create your views here.

def login(request):
    if request.method == 'POST':
        mail = request.POST['email']
        password = request.POST['password']
        User = user.objects.get(email=mail,passeword=password)
        request.session['user'] = User.fname
        data = user.objects.get(fname = User.fname)
        return render(request, 'index.html',{'data':data})
    else:
        return render(request, 'login.html')

def register(request):
    return render(request, 'registration.html')

def index(request):
    return render(request, 'index.html')