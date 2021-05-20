from django.urls import path
from .views import cart_detail,add_cart, remove_item, order_form
app_name='cart'
urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add_cart/<int:id>', add_cart, name='add_cart'),
    path('remove_item/<int:id>', remove_item, name='remove_item'),
    path('order_form/', order_form, name='order_form'),
]
