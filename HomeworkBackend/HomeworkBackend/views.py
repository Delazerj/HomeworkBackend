# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from HomeworkBackend.HomeworkBackend.models import Country
from HomeworkBackend.HomeworkBackend.models import Snowboarder
from HomeworkBackend.HomeworkBackend.serializers import CountrySerializer
from HomeworkBackend.HomeworkBackend.serializers import SnowboarderSerializer


@csrf_exempt
@api_view(['GET','POST'])
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT', 'DELETE'])
def country_detail(request, id):
    try:
        country = Country.objects.get(pk=id)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET','POST'])
def snowboarder_list(request):
    if request.method == 'GET':
        snowboarders = Snowboarder.objects.all()
        serializer = SnowboarderSerializer(snowboarders, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnowboarderSerializer(data=request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT', 'DELETE'])
def snowboarder_detail(request, id):
    try:
        snowboarder = Snowboarder.objects.get(pk=id)
    except Snowboarder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SnowboarderSerializer(Snowboarder)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnowboarderSerializer(snowboarder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snowboarder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)