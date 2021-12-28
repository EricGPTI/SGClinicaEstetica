from django.urls import path
from website.views import home, gallery

urlpatterns = [
    path('', home, name='home'),
    path('gallery', gallery, name='gallery')
]