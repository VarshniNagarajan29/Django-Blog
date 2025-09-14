from django.urls import path
from . import views
from .views import home, about

urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about'),
]