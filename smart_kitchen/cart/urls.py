from django.urls import path
from . import views


app_name = 'cart'


urlpatterns = [
    path('',
         views.cart_detail,
         name='cart_detail'),
    path('add/<int:product_id>/',
         views.cart_add,
         name='cart_add'),
    path('remove/<int:product_id>/',
         views.cart_remove,
         name='cart_remove'),
    path('clear/',
         views.cart_clear,
         name='cart_clear'),
    path('add_random_food/',
         views.cart_add_random_product,
         name='cart_add_random_product'),
    path('add_random_drink/',
         views.cart_add_random_drink,
         name='cart_add_random_drink'),
    path('update_plus/<int:product_id>/',
         views.cart_update_plus,
         name='cart_update_plus'),
    path('update_minus/<int:product_id>/',
         views.cart_update_minus,
         name='cart_update_minus'),
]
