from django.urls import path
from . import views

# url Configuration
urlpatterns = [
    path('hello/', views.say_hello),
    path('hi/', views.say_hi),
    path('posts/', views.blog_list),
    path('posts/<id>/', views.blog_detail),
    path('', views.post_list, name='post_list'),  # List all posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
]