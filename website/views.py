from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'website/index.html')


class Gallery(View):
    def get(self, request):
        return render(request, 'website/galery.html')

class Register(View):
    def get(self, request):
        return render(request, 'website/landpage.html')


