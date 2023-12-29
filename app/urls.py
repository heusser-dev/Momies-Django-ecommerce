from django.urls import path
from .views import home, promociones, pedido,cambiar_estado_pedido,listar_productos,PedidoListCreateView
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', home , name="home"),
    path('promociones/', promociones, name="promociones"),
    path('pedido/', pedido, name="pedido"),
    path('pedidos/', pedido, name='lista_pedidos'),
    path('cambiar_estado/<int:pedido_id>/', cambiar_estado_pedido, name='cambiar_estado_pedido'),
    path('listar_productos', listar_productos, name='listar_productos'),
    path('addpedidos/', PedidoListCreateView.as_view(), name='pedido-list-create'),

]
