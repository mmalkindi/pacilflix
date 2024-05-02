from django.urls import path
from trailer.views import show_main, show_trailer, show_trailer_old

app_name = 'trailer'

urlpatterns = [
    path('main', show_main, name='show_main'),
    path('', show_trailer, name='trailer'),
    path('old', show_trailer_old, name='trailer_old'),
]