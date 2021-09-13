from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home', home, name="home"),
    path('addevent', add_event, name="add_event"),
    path('likedevents', likedevents, name="liked_events"),
    path('home/<int:pk>', liketogglehome, name="like_toggle"),
    path('likedevents/<int:pk>', liketoggleevents, name="like_toggle"),

]
