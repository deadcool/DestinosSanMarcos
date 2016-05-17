from django.db import models
from django.utils import timezone


class Administrador(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    e_mail = models.EmailField(max_length=50)


class Empresa(models.Model):
    nombre = models.TextField(max_length=30)
    RUC = models.IntegerField()
    e_mail = models.EmailField(max_length=30)
    telefono = models.CharField(max_length=12)


class Categoria(models.Model):
    tipo_categoria = models.TextField(max_length=20)


class Privado(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Provincia(models.Model):
    nombre = models.TextField(max_length=20)
    referencia = models.CharField(max_length=100)


class Distrito(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.TextField(max_length=20)
    referencia = models.CharField(max_length=30)


class Destino(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    privado = models.ForeignKey(Privado, on_delete=models.CASCADE)
    nombre = models.TextField(max_length=30)
    direccion = models.CharField(max_length=30)
    foto = models.FileField()
    descripcion = models.TextField(max_length=60)
    calificacion = models.FloatField()


class Comentario(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    nombre_Visit = models.TextField(max_length=30)
    foto_Visit = models.FileField()
    date = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField(max_length=30)
    spam  = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Extras(models.Model):
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    nombre = models.TextField(max_length=20)
    descripcion = models.TextField(max_length=40)
    telefono = models.CharField(max_length=12)
