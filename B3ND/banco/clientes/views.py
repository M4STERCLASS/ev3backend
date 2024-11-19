from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ClienteSerializer

# Vistas tradicionales de Django

# Vista para mostrar todos los clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

# Vista para mostrar los detalles de un cliente específico
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

# Vista para crear un nuevo cliente
def cliente_create(request):
    if request.method == 'POST':
        # Lógica para guardar el cliente (esto se debe implementar)
        pass
    return render(request, 'clientes/cliente_form.html')

# Vista para actualizar un cliente existente
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        # Lógica para actualizar el cliente (esto se debe implementar)
        pass
    return render(request, 'clientes/cliente_form.html', {'cliente': cliente})

# Vista para eliminar un cliente
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('cliente_list')


# Vistas de API (Django REST Framework)

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genero', 'activo', 'nivel_de_satisfaccion']
