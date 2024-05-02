from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', include('show.urls')),
    path('trailer/', include('trailer.urls')),
    path('review/', include('review.urls')),
]
