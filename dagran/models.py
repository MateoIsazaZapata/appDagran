from django.db import models

# Create your models here.
# class Usuarios(models.Model):
#     nombre = models.CharField(max_length=100, null=True)
#     email = models.CharField(max_length=100, null=True)
#     password = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return f"{self.nombre} - {self.email}"

class Alerta(models.Model):
    nombre_alerta = models.CharField(max_length=100, null=True)
    imagen = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre_alerta}"

class Nivel_alerta(models.Model):
    nivel = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.nivel}"

class Reporte(models.Model):
    Alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE, null=True)
    nivel_alerta = models.ForeignKey(Nivel_alerta, on_delete=models.CASCADE, null=True)
    descripcion = models.TextField(null=True)
    fecha = models.DateField(null=True)
    
    if Alerta and nivel_alerta != None:
        def __str__(self):
            return f"{self.Alerta} - {self.nivel_alerta} - {self.descripcion} - {self.fecha}"
    else:
        def __str__(self):
            return f"{self.otro} - {self.nivel_alerta} - {self.descripcion} - {self.fecha}"