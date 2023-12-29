from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework import generics
from .serializers import PedidoSerializer
# Create your views here.
from .models import Producto,Pedido,Categoria
from .forms import ProductoForm


def home(request):
    # Obtén todos los productos desde la base de datos
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    # Manejar el formulario si se envía
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la misma página después de agregar un producto
    else:
        form = ProductoForm()

    # Pasa la lista de productos y el formulario al contexto de la plantilla
    context = {'productos': productos, 'form': form, 'categorias': categorias}


    # Renderiza la plantilla y pasa el contexto
    return render(request, 'app/home.html', context)


def promociones(request):
    return render(request, 'app/promociones.html')

class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

def pedido(request):


    
    pedidos = Pedido.objects.filter (estado = 'en_proceso')
    context = { 'pedidos': pedidos}
    return render(request,'app/pedido.html', context)
    

#Cambiar estado.
def cambiar_estado_pedido(request, pedido_id):
    if request.method == 'POST':
        nuevo_estado = request.POST.get('nuevo_estado')
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.estado = nuevo_estado
        pedido.save()
        messages.success(request, f"Estado del Pedido #{pedido.id} cambiado a {nuevo_estado}.")
        return redirect('lista_pedidos')
    return render(request, 'app/pedido.html')


def listar_productos(request,categoria_id=None):
    categorias = Categoria.objects.all()  # Asegúrate de importar la clase Categoria

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la misma página después de agregar un producto
    else:
        form = ProductoForm()


    if 'categoria_id' in request.GET:
        categoria_id = request.GET['categoria_id']
        productos = Producto.objects.filter(categoria__id=categoria_id)
    else:
        productos = Producto.objects.all()

    context = {'productos': productos, 'form': form, 'categorias': categorias}



    return render(request, 'app/listar_productos.html', context)