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

class Corporal(View):
    def get(self, request):
        return render(request, 'website/corporal.html')


class Facial(View):
    def get(self, request):
        return render(request, 'website/facial.html')


class Basica(View):
    def get(self, request):
        return render(request, 'website/basica.html')


class Varize(View):
    def get(self, request):
        return render(request, 'website/varizes.html')


class Laser(View):
    def get(self, request):
        return render(request, 'website/laser.html')


class Olhos(View):
    def get(self, request):
        return render(request, 'website/olhos.html')


