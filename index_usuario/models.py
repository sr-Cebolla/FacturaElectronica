from django.db import models

class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Definicion(models.Model):
    id_definicion = models.AutoField(primary_key=True)
    titulo_definicion = models.CharField(max_length=30)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo_definicion

class EconomiaEmisores(models.Model):
    id_economia_emisores = models.AutoField(primary_key=True)
    impacto = models.TextField()
    consecuencias = models.TextField()
    cumplimiento_fiscal = models.TextField()

    def __str__(self):
        return self.impacto

class Poblacion(models.Model):
    id_poblacion = models.AutoField(primary_key=True)
    impacto = models.TextField()
    consecuencias = models.TextField()
    cambio_cultural = models.TextField()
    beneficios_sociales = models.TextField()
    seguridad_de_datos = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.impacto

class MedioAmbiente(models.Model):
    id_medio_ambiente = models.AutoField(primary_key=True)
    beneficios_generados = models.TextField(null=True, blank=True)
    info_reduccion_residuos = models.TextField(null=True, blank=True)
    beneficios_ecologicos = models.TextField(null=True, blank=True)
    ahorro_recursos = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.beneficios_generados

class MetodoEvacion(models.Model):
    id_metodo_evacion = models.AutoField(primary_key=True)
    nombre_metodo = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_metodo

class EvacionImpuestos(models.Model):
    id_evacion_impuestos = models.AutoField(primary_key=True)
    id_metodo_evacion = models.ForeignKey(MetodoEvacion, on_delete=models.CASCADE)
    riesgos_asociados = models.TextField()

    def __str__(self):
        return self.riesgos_asociados

class Efectos(models.Model):
    id_efectos = models.AutoField(primary_key=True)
    id_efecto_poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE)
    id_efecto_medio_ambiente = models.ForeignKey(MedioAmbiente, on_delete=models.CASCADE)
    id_efecto_evacion_impuestos = models.ForeignKey(EvacionImpuestos, on_delete=models.CASCADE)
    id_efecto_economia_emisores = models.ForeignKey(EconomiaEmisores, on_delete=models.CASCADE)

    def __str__(self):
        return f"Efectos {self.id_efectos}"

class Emisores(models.Model):
    id_emisores = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"{self.fecha}"

class Informacion(models.Model):
    id_informacion = models.AutoField(primary_key=True)
    id_definicion = models.ForeignKey(Definicion, on_delete=models.CASCADE)
    id_emisores = models.ForeignKey(Emisores, on_delete=models.CASCADE)
    id_efectos = models.ForeignKey(Efectos, on_delete=models.CASCADE)
    ventajas = models.TextField()
    desventajas = models.TextField()
    requerimientos = models.TextField()

    def __str__(self):
        return self.requerimientos
