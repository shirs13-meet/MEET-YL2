from django.shortcuts import render
from django.http import HttpResponse

from models import Poll, Answer

def Thanks(request):
	return HttpResponse("Thank you for voting!")

