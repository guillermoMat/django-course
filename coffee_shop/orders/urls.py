
from django.urls import path
#from django.contrib.auth.views import LogoutView
from .views import MyOrderView,CreateOrderProductView


urlpatterns = [
     path("misOrdenes/", MyOrderView.as_view(), name="misOrdenes"),
     path('agregar-producto/',CreateOrderProductView.as_view(),name='addProduct'),
]
