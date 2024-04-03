from django.shortcuts import render
from .models import *
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,ListAPIView
from . import serializers


class AdvertisingAPIView(RetrieveAPIView,UpdateAPIView):
    queryset = Advertising.objects.all()
    serializer_class = serializers.AdvertisingSerializer

class GroupsAPIView(ListAPIView,UpdateAPIView):
    queryset = Groups.objects.all()
    serializer_class  = serializers.GroupsSerializer