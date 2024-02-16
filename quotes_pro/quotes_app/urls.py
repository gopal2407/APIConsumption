from django.urls import path
from .views import quotes_show, quotes_update, quotes_delete,quotes_data


urlpatterns = [
    path('show/', quotes_show, name='quotes_show_url'),
    path('data/', quotes_data, name='quotes_data_url'),
    path('update/<int:pk>/', quotes_update, name='quotes_update_url'),
    path('delete/<int:pk>/', quotes_delete, name='quotes_delete_url'),
]