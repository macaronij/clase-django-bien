from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Dirreccion Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fechad de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    #funcion de la clase Project
    def __str__(self):
        return self.title
    #clase de la clase Project
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural ="proyectos"
        ordering = ["-created"]
