from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.content, name='content'),
    path('cv', views.cv, name='cv'),
    path('about', views.about, name='about'),
]
