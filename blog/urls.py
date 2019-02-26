from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog_list', views.blog_list, name='blog_list'),
    path('blog_new', views.blog_new, name='blog_new'),
    path('blog_edit/<int:pk>', views.blog_edit, name='blog_edit'),
]