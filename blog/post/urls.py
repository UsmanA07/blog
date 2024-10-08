from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
]
