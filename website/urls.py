from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from website import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('register/', views.Register.as_view(), name='register'),
    path('corporal/', views.Corporal.as_view(), name='corporal'),
    path('facial/', views.Facial.as_view(), name='facial'),
    path('basica/', views.Basica.as_view(), name='basica'),
    path('varize/', views.Varize.as_view(), name='varize'),
    path('laser/', views.Laser.as_view(), name='laser'),
    path('olhos/', views.Laser.as_view(), name='olhos'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)