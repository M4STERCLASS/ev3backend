from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # ruta para el panel de administración de Django
    path('clientes/', include('clientes.urls')),  # incluye las URLs de la aplicación 'clientes'
]
