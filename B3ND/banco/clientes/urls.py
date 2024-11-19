from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet
from django.urls import path
from .views import cliente_list, cliente_detail, cliente_create, cliente_update, cliente_delete


router = DefaultRouter()
router.register(r'', ClienteViewSet)

urlpatterns = [
    path('', cliente_list, name='cliente_list'),
    path('<int:pk>/', cliente_detail, name='cliente_detail'),
    path('crear/', cliente_create, name='cliente_create'),
    path('<int:pk>/editar/', cliente_update, name='cliente_update'),
    path('<int:pk>/eliminar/', cliente_delete, name='cliente_delete'),
    path('api/', include(router.urls)),
]
