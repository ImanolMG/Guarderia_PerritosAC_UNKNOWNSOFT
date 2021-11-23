from django.urls import path
from . import views
from .views import registrar_cliente, eliminar_cliente


urlpatterns = [

    path('registrarcliente/', registrar_cliente),
    path('eliminarcliente/<id>', eliminar_cliente)

]