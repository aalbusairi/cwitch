from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

def usersignup(request):
	context = {}
	form = UserSignup()
	context['form'] = form
	if request.method == 'POST':
		form = UserSignup(request.POST)
		if form.is_valid():
			user = form.save()
			username = user.username
			password = user.password

			user.set_password(password)
			user.save()

			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)
			return redirect("games:login")
			
		messages.error(request, form.errors)
		
	return render(request, 'signup.html', context)

def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form
	if request.method == 'POST':
		form = UserLogin(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("games:login")
				

			messages.error(request, "Wrong username/password combination. Please try again.")
			return redirect("games:login")
		messages.error(request, form.errors)
		
	return render(request, 'login.html', context)

def userlogout(request):
	logout(request)
	return redirect("games:login")
