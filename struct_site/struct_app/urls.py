from django.urls import path,include
from .views import *

urlpatterns = [
    path('allgroup', GroupListView.as_view(), name='group-list'),
    path('group/<slug:group_slug>/', UnitsListView.as_view()),
    path('group', UnitsListView.as_view()),
]