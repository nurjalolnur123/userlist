from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('people/add', add_people, name="add_people")
]