from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('group/all/', GroupListView.as_view()),
    re_path(r"group/detail/(?P<tree_hierarchy>.*)", GroupDetailView.as_view()),
    re_path(r'.units', UnitsListView.as_view(),)
]