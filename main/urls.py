from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('add_suggestion/', add_suggestion, name='add_suggestion')

]
