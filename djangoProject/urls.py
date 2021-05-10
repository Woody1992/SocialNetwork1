from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls', namespace='landing')),
    path('accounts/', include('allauth.urls')),
    path('social/', include('social.urls', namespace='social')),
]
