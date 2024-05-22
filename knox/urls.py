from django.urls import re_path

from knox import views

urlpatterns = [
    re_path(r'login/', views.LoginView.as_view(), name='knox_login'),
    re_path(r'logout/', views.LogoutView.as_view(), name='knox_logout'),
    re_path(r'logoutall/', views.LogoutAllView.as_view(), name='knox_logoutall'),
]
