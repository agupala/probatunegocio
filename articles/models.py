from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = RichTextField(verbose_name="Descripción")
    price = models.FloatField(verbose_name="Precio", editable=True)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Foto principal")
    image_thumbnail = ImageSpecField(
        source='photo_main',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 60}
    )
    link_mp = models.URLField(null=True, blank=True, verbose_name="Link a Mercado Pago")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True, verbose_name="Foto 1")
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, null=True, verbose_name="Foto 2")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "articulo"
        verbose_name_plural = "articulos"
        ordering = ['-created']

    def __str__(self):
        return self.name


