from django.urls import path,include
from .views import *

urlpatterns = [
    path('allgroup', GroupListView.as_view(), name='group-list'),
    path('group', UnitsListView.as_view(), name='units-in-group-list'),
]