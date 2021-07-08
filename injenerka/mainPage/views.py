from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
	return render(request, 'index.html')
