from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_title_view, name='generate_title'),
]
