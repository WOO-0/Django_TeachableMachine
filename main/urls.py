from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('signin', views.SigninView.as_view(), name='signin'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('home', views.HomeView.as_view(), name='home'),
    path('test', views.TestView.as_view(), name='test')
]