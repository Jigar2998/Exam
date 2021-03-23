from django.shortcuts import render, redirect
from django.http import request
from .models import user
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    return redirect('login')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        print(fname)
        lname = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        dob = request.POST['dob']
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        mobile = request.POST['mobile']
        address = request.POST['address']
        password = request.POST['password']
        User = user(fname=fname, lname=lname, email=email, mobile=mobile, gender=gender,
                    birth_date=dob, address=address, image=image, passeword=password)
        User.save()
        text = 'Registration Successfully completed'
        return render(request, 'registration.html', {'text': text})
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        mail = request.POST['email']
        password = request.POST['password']
        User = user.objects.get(email=mail, passeword=password)
        request.session['user'] = User.fname
        data = user.objects.get(fname=User.fname)
        return render(request, 'index.html', {'data': data})
    else:
        return render(request, 'login.html')


def index(request):
    if 'user' in request.session:
        return render(request, 'index.html')
    else:
        return redirect('login')


def profile(request):
    if 'user' in request.session:
        User = user.objects.get(fname=request.session['user'])
        return render(request, 'profile.html', {'User': User})
    else:
        return redirect('login')


def edit_profile(request, id):
    if 'user' in request.session:
        if request.method == 'POST':
            User = user.objects.get(fname=request.session['user'])
            fname = request.POST['fname']
            print(fname)
            lname = request.POST['lname']
            email = request.POST['email']
            gender = request.POST['gender']
            dob = request.POST['dob']
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
            mobile = request.POST['mobile']
            address = request.POST['address']
            request.session['user']=fname
            user.objects.all().filter(id=id).update(fname=fname,lname=lname,email=email,mobile=mobile,gender=gender,birth_date=dob,address=address,image=image)
            return redirect('profile')
        else:
            data = user.objects.get(id=id)
            return render(request, 'edit_profile.html', {'data': data})
    else:
        return redirect('login')

def change_password(request,id):
    if 'user' in request.session:
        if request.method == 'POST':
            data = user.objects.get(fname=request.session['user'])
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            try:
                user.objects.get(passeword=old_password)
                user.objects.all().filter(id=id).update(passeword=new_password)
                text = "Your Password Is Change"
                return render(request, 'change_password.html',{'text':text})
            except:
                false = "Old Password is Not Match"
                return render(request, 'change_password.html',{'false':false})
        else:
            return render(request, 'change_password.html',)
    else:
        return redirect('login')