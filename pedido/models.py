from django.db import models

class Pedido(models.Model):
    nombre = models.CharField(max_length = 20, blank = False, null = False)
    email = models.EmailField(blank=False, null=False)
    asunto = models.CharField(max_length = 80, blank = False, null = False)
    mensaje = models.CharField(max_length = 500, blank = False, null = False)
    timestamp = models.DateTimeField(auto_now_add=True)
