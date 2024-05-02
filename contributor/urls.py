from django.urls import path
from contributor.views import show_main

app_name = 'contributor'

urlpatterns = [
path('', show_main, name='show_main'),
]