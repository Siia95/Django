from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('add_quote/', views.add_quote, name='add_quote'),
    path('list/', views.quote_list, name='quote_list'),
]
