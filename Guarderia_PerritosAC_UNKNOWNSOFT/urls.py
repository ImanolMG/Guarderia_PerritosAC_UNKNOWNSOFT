"""Guarderia_PerritosAC_UNKNOWNSOFT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.preregistro, name='preregistro')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='preregistro')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from preregistro.views import pagina_principal, formulario_preregistro, registrar_cliente, administracion_clientes, eliminar_cliente
urlpatterns = [
    path('', pagina_principal),
    path('preregistro/', formulario_preregistro),
    path('admin/', admin.site.urls),
    path('registrarcliente/', registrar_cliente),
    path('administracion/', administracion_clientes),
    path('eliminarcliente/<id>', eliminar_cliente)
]
