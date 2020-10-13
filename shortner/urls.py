
from django.contrib import admin
from django.urls import path, include
from .views import HomeView, give
from . import views as v



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('u/<str:code>', give),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login', v.LoginView.as_view(), name='login'),
    path('logout', v.LogoutView.as_view(), name='logout'),
]
