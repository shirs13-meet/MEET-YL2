from django.shortcuts import render
from django.http import HttpResponse

from models import Poll, Answer

def Thanks(request):
	return HttpResponse("Thank you for voting!")

def contact(request):
	return render(request, "contactme.html")

def homepage(request):
	return render(request, "mypage.html")

