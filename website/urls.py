from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from website import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('register/', views.Register.as_view(), name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)