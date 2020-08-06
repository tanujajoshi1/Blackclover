
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import User, Photo
from .forms import PhotoForm

# Create your views here.

def index(request):
	return render(request,"myproject/index.html")


def login_view(request):
	if request.method=="GET":
		return render(request,"myproject/login.html")

	else:
		username=request.POST["username"]
		password=request.POST["password"]
		user=authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request,"myproject/login.html",{"message":"Invalid username / password"})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))

def register(request):
	if request.method=="POST":	
		username=request.POST["username"]
		email=request.POST["email"]
		password=request.POST["password"]
		confirmation=request.POST["confirmation"]

		if password!=confirmation:
			return render(request,"myproject/register.html",{"message":"Password must match"})

		try:
			user=User.objects.create_user(username,email,password)
			user.save()

		except IntegrityError:
			return render(request,"myproject/register.html",{"message": "This username already exist"})
		login(request,user)
		return HttpResponseRedirect(reverse("index"))

	else:
		return render(request,"myproject/register.html")



def getstarted(request,username):
	if request.user.username:
		return HttpResponseRedirect(reverse("photo_list"))		
	else:		
		return HttpResponseRedirect(reverse("login"))

def photo_list(request):
	photos=Photo.objects.all()
	if request.method=='POST':
		form=PhotoForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('photo_list')


	else:
		form=PhotoForm()
	return render(request, 'myproject/photo_list.html',{'form':form, 'photos':photos})
	
def learn(request):
	return render(request,"myproject/learn.html")

        
    



