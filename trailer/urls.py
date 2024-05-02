from django.urls import path
from trailer.views import show_main, show_trailer

app_name = 'trailer'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('trailer', show_trailer, name='trailer'),
]