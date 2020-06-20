from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_content, name='post_content'),
    path('cv', views.cv, name='cv'),
    path('about', views.about, name='about'),
]
