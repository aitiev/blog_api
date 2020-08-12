from django.urls import path

from .views import posts_list


urlpatterns = [
    path('posts/', posts_list, name='posts-list'),
]
