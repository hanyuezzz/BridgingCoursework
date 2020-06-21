from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv, name='cv'),
    path('education/new/', views.education_new, name='education_new'),
    path('education/remove/<pk>/', views.education_remove, name='education_remove'),
    path('achievement/new/', views.achievement_new, name='achievement_new'),
    path('achievement/remove/<pk>/', views.achievement_remove, name='achievement_remove'),
    path('skill/new/', views.skill_new, name='skill_new'),
    path('skill/remove/<pk>/', views.skill_remove, name='skill_remove'),
    path('course/new/', views.course_new, name='course_new'),
    path('course/remove/<pk>/', views.course_remove, name='course_remove'),
]
