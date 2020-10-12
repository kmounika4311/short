from django.shortcuts import HttpResponse, render, get_object_or_404
from django.views import View
from .forms import UrlForm
from .models import ShortUrl

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        url = request.POST.get('url', None)
        if url == None:
            return HttpResponse("Please Enter Url")
        url_model = ShortUrl.objects.create(url=url)
        url_model.code = url_model.generate_code()
        print(url_model.code)
        url_model.save()
        return HttpResponse(url_model.code)

def give(request, code):
    url = get_object_or_404(ShortUrl, code=code)
    return render(request, 'redirect.html', context = {'url': url.url})
