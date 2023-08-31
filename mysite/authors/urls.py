from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('create_author/', views.create_author, name='create_author'),
    path('<int:author_id>/', views.author_detail, name='author_detail'),
    path('author_list/', views.author_list, name='author_list'),
    path('<int:author_id>/delete/', views.author_delete, name='author_delete'),

]
