from django.urls import path
from .views import index, about

urlpatterns = [
    path('about/', about, name='about'),
    path('', index, name='index'),

]