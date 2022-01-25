from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializers
from .models import Person
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/api/list/',
        'Detail': '/api/detail/<str:pk>/',
        'Create': '/api/create/',
        'Update': '/api/update/<str:pk>/',
        'Delete': '/api/delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def personList(request):
    person = Person.objects.all()
    serializr = PersonSerializers(person, many=True)
    return Response(serializr.data)

@api_view(['GET'])
def personDetail(request, pk):
    person = Person.objects.get(id=pk)
    serializr = PersonSerializers(person, many=False)
    return Response(serializr.data)

@api_view(['POST'])
def personCreate(request):
    serializr = PersonSerializers(data=request.data)
    if serializr.is_valid():
        serializr.save()
    return Response(serializr.data)

@api_view(['POST'])
def personUpdate(request, pk):
    person = Person.objects.get(id=pk)
    serializr = PersonSerializers(instance=person, data=request.data)
    if serializr.is_valid():
        serializr.save()
    return Response(serializr.data)

@api_view(['DELETE'])
def personDelete(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return Response("Deleted")
