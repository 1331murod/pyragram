from django.urls import path
from .views import *


urlpatterns = [
    path("reklama/<int:pk>/",AdvertisingAPIView.as_view()),
    path("groups/",GroupsAPIView.as_view())
]