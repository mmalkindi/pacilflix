from django.urls import path
from show.views import show_main, show_tayangan, show_series, show_film, show_episode

app_name = 'show'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('tayangan/', show_tayangan, name='tayangan'),
    path('series/', show_series, name='series'),
    path('film/', show_film, name='film'),
    path('episode/', show_episode, name='episode'),
]
