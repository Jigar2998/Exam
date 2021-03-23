from django.shortcuts import render, redirect
from django.http import request
from .models import user,contact,task_assign
from django.core.files.storage import FileSystemStorage
import smtplib
from django.core.mail import send_mail

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
        send_mail('Registered Successfully', f'Hello {fname} \n You Are registered Successfuly in Our System!', 'jigarramani40@gmail.com', [f'{email}'])
        return render(request, 'registration.html', {'text': text})
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        mail = request.POST['email']
        password = request.POST['password']
        try:
            User = user.objects.get(email=mail, passeword=password)
            request.session['user'] = User.fname
            data = user.objects.get(fname=User.fname)
            return redirect('index')
        except:
            text = 'Invalid Login Credential'
            return render(request, 'login.html',{'text':text})
    else:
        return render(request, 'login.html')


def index(request):
    if 'user' in request.session:
        data = user.objects.get(fname=request.session['user'])
        return render(request, 'index.html',{'data':data})
    else:
        return redirect('login')


def task_list(request):
    if 'user' in request.session:
        data = user.objects.get(fname=request.session['user'])
        task = task_assign.objects.all().filter(assign_user_id=data.id)
        return render(request, 'task_list.html',{'data':data,'task':task})
    else:
        return redirect('login')

def update_status(request,id):
    if 'user' in request.session:
        data = user.objects.get(fname=request.session['user'])
        if request.method == 'POST':
            status = request.POST['status']
            task_assign.objects.all().filter(id=id).update(status=status)
            return redirect('task_list')
        else:
            return render(request, 'update_status.html',{'data':data})
    else:
        return redirect('login')

def profile(request):
    if 'user' in request.session:
        data = user.objects.get(fname=request.session['user'])
        User = user.objects.get(fname=data.fname)
        return render(request, 'profile.html', {'data': data,'User':User})
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
        data = user.objects.get(fname=request.session['user'])
        if request.method == 'POST':
            data = user.objects.get(fname=request.session['user'])
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            try:
                user.objects.get(passeword=old_password)
                user.objects.all().filter(id=id).update(passeword=new_password)
                text = "Your Password Is Change"
                return render(request, 'change_password.html',{'text':text,'data':data})
            except:
                false = "Old Password is Not Match"
                return render(request, 'change_password.html',{'false':false,'data':data})
        else:
            return render(request, 'change_password.html',{'data':data})
    else:
        return redirect('login')

def contact(request):
    if request.method == 'POST':
        fname = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact = contact(name=fname, email=email, message=message)
        Contact.save()
        return redirect('index')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('login')
    else:
        return redirect('login')