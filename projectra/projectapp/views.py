from django.shortcuts import render, redirect
from .forms import UserLoginForms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import studentformsave

from django.core.mail import send_mail
from django.conf import settings


@login_required(login_url='login')
def index(request):
	return render(request, 'index.html')


def get_registration(request):
	form = UserCreationForm() 
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			print("Wrong")
	context = {'form': form}
	return render(request, 'loginfile/registration.html', context)



def get_login(request):
	forms = UserLoginForms()
	if request.method == 'POST':
		forms = UserLoginForms(request.POST)
		if forms.is_valid():
			username = forms.cleaned_data['username']
			password = forms.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return redirect('/')
			else:
				print("Login Faild")
	contex = {'forms': forms}
	return render(request, 'loginfile/login.html', contex)


def get_logout(request):
	logout(request)
	return redirect('login')


def stformfil(request):
	return render(request, 'stdformfilup.html')



def stdsave(request):
	print(request.POST)
	applicant_name = request.GET['applicant_name']
	father_name = request.GET['father_name']
	mother_name = request.GET['mother_name']
	phonenumber = request.GET['phonenumber']
	dateofbirth = request.GET['dateofbirth']
	address = request.GET['address']
	city = request.GET['city']
	departsubject = request.GET['departsubject']
	
	stdform = studentformsave(applicant_name=applicant_name, father_name=father_name, mother_name=mother_name, phonenumber=phonenumber,dateofbirth=dateofbirth,address=address,city=city,departsubject=departsubject)
	stdform.save()
	return redirect('/')


def student(request):
	data1 = studentformsave.objects.all()
	return render(request, 'student.html',{'data1':data1})



def teacher(request):
	return render(request, 'teacher.html')


def mailsending(request):
	return render(request, 'mailing.html')


def datasending(request):
	if request.method == 'POST':
		message = request.POST['message']
		subject = request.POST['subject']
		to = request.POST['to']
		send_mail(subject,
			message, settings.EMAIL_HOST_USER, 
			[to],
			fail_silently=False)
	return render(request,'mailing.html')
	