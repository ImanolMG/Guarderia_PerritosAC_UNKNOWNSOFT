from django.urls import path
from . import views
from .views import registrar_cliente


urlpatterns = [

    path('registrarcliente/', registrar_cliente),


]