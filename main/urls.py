from django.urls import path
from .views import get_first_page, createProduct, show_dict

urlpatterns = [
    path('', show_dict, name='show_dict'),
    # path('', get_first_page, name='first_page'),
    path('create/', createProduct, name='create'),
]
