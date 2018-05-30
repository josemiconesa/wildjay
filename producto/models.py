import uuid
from django.db import models

def producto_image(instance, filename):
    return 'product_{0}/{1}/{2}'.format(instance.nombre, uuid.uuid4(), filename)


class Producto(models.Model):
    #Categorias
    CHAQUETA = 'CH'
    CAMISETA = 'CA'
    PANTALON = 'PA'
    ACCESORIO = 'AC'

    CATEGORIAS = (
        (CHAQUETA, 'Chaqueta'),
        (CAMISETA, 'Camiseta'),
        (PANTALON, 'Pantalon'),
        (ACCESORIO, 'Accesorio')

    )

    #Tallas
    TALLAS = (
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL')
    )

    nombre = models.CharField(max_length=120, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False, default=0)
    descripcion = models.CharField(max_length=500)
    categoria = models.CharField(
        max_length=2,
        choices=CATEGORIAS,
        default=CHAQUETA
    )
    talla = models.CharField(
        max_length=5,
        choices=TALLAS,
        default='L',
        null=True,
        blank=True
    )
    imagen = models.ImageField(upload_to=producto_image, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Producto {}'.format(self.nombre)
