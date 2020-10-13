from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from django.views import View
from .forms import UrlForm, LoginForm
from .models import ShortUrl
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout



class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            urls = ShortUrl.objects.filter(user=request.user)
            return render(request, 'index.html', context={'urls': urls})
        else:
            return render(request, 'index.html')
    
    def post(self, request):
        if request.user.is_authenticated:
            url = request.POST.get('url', None)
            if url == None:
                return HttpResponse("Please Enter Url")
            url_model = ShortUrl.objects.create(url=url, user=request.user)
            url_model.code = url_model.generate_code()
            print(url_model.code)
            url_model.save()
            return HttpResponse(url_model.code)

def give(request, code):
    url = get_object_or_404(ShortUrl, code=code)
    return render(request, 'redirect.html', context = {'url': url.url})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse("<h1>Already Log in, Please Log Out First</h1>")
        form = AuthenticationForm()
        return render(request, 'registration/login.html', context={'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        return HttpResponse("<h1>Erorr</h1>")

class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse("<h1>Not Log In.</h1>")
        else:
            logout(request)
            return redirect('/')


