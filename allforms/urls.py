from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('coming_soon/', TemplateView.as_view(template_name='coming_soon.html'), name='coming_soon'),
]
