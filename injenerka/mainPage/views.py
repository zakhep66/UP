from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer


def index(request):
	return render(request, 'index.html')


def home(request):
	return render(request, 'home.html')


def lending(request):
	context = {
		'first_name': request.user.first_name,
		'last_name': request.user.last_name,
		'date_joined': request.user.date_joined,
		'email': request.user.email,
	}
	return render(request, 'lending.html', context)


#######################################
###############customer################
#######################################
# @api_view(['GET', 'POST'])
# def customer_list(request):
#
# 	if request.method == 'GET':
# 		customer = Customer.objects.all()
# 		serializer = CustomerSerializer(customer, many=True)
# 		return Response(serializer.data)
#
# 	elif request.method == 'POST':
# 		serializer = CustomerSerializer(data=request.data)
#
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
	try:
		customer = Customer.objects.get(pk=pk)

	except Customer.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CustomerSerializer(customer)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = CustomerSerializer(customer, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		customer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
#######################################
##############/customer################
#######################################
