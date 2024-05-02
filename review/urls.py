from django.urls import path
from review.views import show_main, show_ulasan

urlpatterns = [
    path('', show_main, name='show_main'),
    path('ulasan', show_ulasan, name='ulasan'),
]
