
from django.contrib import admin
from django.urls import path
from .views import HomeView, give

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('u/<str:code>', give)
]
