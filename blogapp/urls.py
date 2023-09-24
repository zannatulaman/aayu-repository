from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]