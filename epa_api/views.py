from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, routers
from rest_framework.parsers import JSONParser
from rest_framework.request import Request

from epa_frontend.models import Profile, Events, Merchants, EventsType
from epa_api.serializers import UserSerializer, EventsSerializer, MerchantsSerializer, EventsTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer


class EventsListView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class MerchantsListView(viewsets.ModelViewSet):
    queryset = Merchants.objects.all()
    serializer_class = MerchantsSerializer


class EventsTypeListView(viewsets.ModelViewSet):
    queryset = EventsType.objects.all()
    serializer_class = EventsTypeSerializer
# @csrf_exempt
# def event_detail(request, pk):
#     """
#     Retrieve, update or delete an event.
#     """
#     try:
#         event = Events.objects.get(pk=pk)
#     except Events.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = EventsSerializer(event)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = EventsSerializer(event, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
