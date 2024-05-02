from django.urls import path
from subscription.views import show_main, show_buy_page

app_name = 'subscription'

urlpatterns = [
path('', show_main, name='show_main'),
path('buy/', show_buy_page, name='show_buy_page')
]