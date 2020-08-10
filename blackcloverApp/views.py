from django.http import HttpResponse
## from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Appointment
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def index(request):
    return render(request, "blackcloverApp/index.html")
def appointment(request):
      # POST
  if request.method == 'POST':
      # Save order data to the database
    add = Appointment(
              fname=request.POST.get('fname'),
              lname=request.POST.get('lname'),
              phone=request.POST.get('phone'),
              email=request.POST.get('email'),              
              doctor=request.POST.get('doctor'),
              date=request.POST.get('date'),
              time=request.POST.get('time'),
              comment=request.POST.get('comment'),
            )

    add.save()

    if add is not None:
     context = {
      "patient": Appointment.objects.last(),
     }
     return render(request, "blackcloverApp/index.html", context)
    else:
      return HttpResponse('{"success": false, "message": "Invalid input"}')

 # GET
  else:
    return render(request, "blackcloverApp/appointment.html")

def login_view(request):
  # POST
  if request.method == 'POST':    
    username = request.POST["username"]
    password = request.POST["password"]    
    if username == '' or password == '':
      return HttpResponse('{"success": false, "message": "Both username and password are required."}')
    
    
    # Django built-in username & password authentication + login session --     
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponse('{"success": true, "message": ""}')
    
    else:
      return HttpResponse('{"success": false, "message": "Invalid username and/or password."}')
  
  else:
    return render(request, "blackcloverApp/appointment.html")




def logout_view(request):
  if request.method=='GET':
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# ============================ REGISTER ==========================================

def register_view(request): 
  username = request.POST['username']
  password = request.POST['password']
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  
  
  if username == '' or password == '' or first_name == '' or last_name == '' or email == '':
    return HttpResponse('{"success": false, "message": "All fields must be completed."}')
    
  try:
    User.objects.get(username=username)
    return HttpResponse('{"success": false, "message": " ERROR! Username already exists."}')
  except:
   
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()    
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponse('{"success": true, "message": "Successfuly Registered"}')

