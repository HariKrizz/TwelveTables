from django.urls import path
from . import views

urlpatterns = [
    path('cart_details',views.cart_details,name='cart_details'),
    path('add_cart/<int:prdct_id>',views.add_cart,name='add_cart'),
    path('decrement_cart/<int:prdct_id>',views.decrement_cart,name='decrement_cart'),
    path('delete_cart/<int:prdct_id>',views.delete_cart,name='delete_cart')
]


#                  