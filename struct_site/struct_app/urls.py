from django.urls import path,include
from .views import *

urlpatterns = [
    path('', GroupListView.as_view(), name='group-list'),


]