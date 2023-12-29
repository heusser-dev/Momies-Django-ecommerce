from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descuento = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    cantidad = models.IntegerField(default=0)
    comentario = models.CharField(max_length=100,default="")


    SIMPLE = 'Simple'
    DOBLE = 'Doble'
    OPCIONES_HAMBURGUESA = [
        (SIMPLE, 'Hamburguesa Simple'),
        (DOBLE, 'Hamburguesa Doble'),
    ]

    # Agregar el campo de elección
    tipo_hamburguesa = models.CharField(
        max_length=10,
        choices=OPCIONES_HAMBURGUESA,
        default=SIMPLE,
    )
    

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    productos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_total(self):
        # Método para calcular el total del carrito basado en los productos actuales
        self.total = sum(producto.precio for producto in self.productos.all())
        self.save()

    def agregar_producto(self, producto):
        # Método para agregar un producto al carrito
        self.productos.add(producto)
        self.calcular_total()

    def quitar_producto(self, producto):
        # Método para quitar un producto del carrito
        self.productos.remove(producto)
        self.calcular_total()

    def limpiar_carrito(self):
        # Método para vaciar el carrito
        self.productos.clear()
        self.total = 0.00
        self.save()

    def __str__(self):
        return f"Carrito {self.id}"

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('en_proceso', 'En proceso'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]
    productos = models.ManyToManyField(Producto)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    direccion_entrega = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='en_proceso')
    imagen = models.ImageField(upload_to="pedidos", null=True)
    nombre_cliente = models.CharField(max_length=36 ,null=True)

    # Agrega otros campos relacionados con el pedido según tus necesidades

    def __str__(self):
        return f"Pedido #{self.id} - {self.estado}"


# Create your models here.
