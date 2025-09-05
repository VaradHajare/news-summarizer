from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch_article/', views.fetch_full_article, name='fetch_full_article'),
]
