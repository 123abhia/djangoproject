from django.urls import path
from .views import *



urlpatterns = [
    path('pro',Produlist.as_view(),name="p"),
    path('product/<int:id>',Detailist.as_view(),name="product"),
    path('cl/<int:pid>',CheckoutView.as_view(),name='cl'),
    path('ods',OrderListv.as_view(),name="orders"),
     path('delcart/<int:id>',Delete , name='dlt'),
   
    
]