from django.urls import path
from acnt.views import *




urlpatterns = [

    path('reg',Register.as_view(),name="reg"),
    path( "sign",Signin.as_view(),name="sign"),
    path( "lgout",Lgout.as_view(),name="f"),
   
          
            
]