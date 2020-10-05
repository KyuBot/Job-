from django.urls import path
from . import views

app_name = 'recruitments'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:recruitment_pk>/', views.detail, name='detail'),
    path('<int:recruitment_pk>/introductions/', views.introduction_list, name='introduction_list'),
    path('<int:recruitment_pk>/introductions/create/', views.introduction_create, name='introduction_create'),
    path('<int:recruitment_pk>/introductions/<int:introduction_pk>/', views.introduction_detail, name='introduction_detail'),
    path('<int:recruitment_pk>/apply/<int:article_pk>/', views.apply, name='views.apply'),
]