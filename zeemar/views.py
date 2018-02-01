from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'zeemar/index.html')

def umrah(request):
	return render(request,'zeemar/umrah.html')
