from django.contrib.auth.models import User
from django.db import models

categoriavehiculos= [
    (1,'ligeros'),
    (2,'pesados'),
    (3,'especiales'),
    (4,'agricolas'),
    (5,'otros')
]

class cliente(models.Model):
    cedula= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    direccion= models.CharField(max_length=250)
    telefono= models.CharField(max_length=10)
    username= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class vehiculos(models.Model):
    marca= models.CharField(max_length=200)
    modelo= models.CharField(max_length=200)
    año= models.IntegerField()
    precio= models.FloatField()
    usado= models.BooleanField(default=False)
    imagen= models.URLField()
    vendido= models.BooleanField(default=False,null=True)
    creadopor= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.año}"

class factura(models.Model):
    cliente= models.ForeignKey(cliente,on_delete=models.CASCADE)
    vehiculo_comprado= models.ForeignKey(vehiculos,on_delete=models.CASCADE)
    fecha= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} {self.fecha}"

class categoria_vehiculos(models.Model):
    vehiculos= models.ForeignKey(vehiculos,on_delete=models.CASCADE)
    categoria= models.IntegerField(null=False,blank=False, choices= categoriavehiculos)

    def __str__(self):
        return f"{self.vehiculos} categoria {self.categoria}"


    

