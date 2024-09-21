# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signUp, name='signUp'),
    path('create_blog/', views.create_post, name='create_blog'),
    path('show_blog/', views.show_posts, name='show_blog'),
    path('update//<int:id>/', views.update_post, name='update_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('', views.home, name='home'),  
]
