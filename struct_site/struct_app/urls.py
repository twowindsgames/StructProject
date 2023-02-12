from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('group/all/', GroupListView.as_view({'get': 'list'})),
    re_path(r"group/(?P<tree_hierarchy>.*)", GroupDetailView.as_view()),
    re_path(r'.*employees', EmployeeListView.as_view(), )
]
