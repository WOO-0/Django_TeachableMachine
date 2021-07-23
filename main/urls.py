from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    # path('signin', views.SigninView.as_view(), name='signin'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('home', views.HomeView.as_view(), name='home'),
    path('record', views.RecordView.as_view(), name='record'),

    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
    path('kakao/logout/', views.kakao_logout, name='kakao_logout'),
]