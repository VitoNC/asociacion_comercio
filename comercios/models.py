from django.db import models
from django import forms

from modelcluster.fields import ParentalManyToManyField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


from wagtail.snippets.models import register_snippet

from wagtail.search import index


# Create your models here.



class ComercioIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)

        categoria = request.GET.get('categoria')
        

        entradas = Comercio.objects.all()

        context['comercios'] = entradas

        return context

    subpage_types = ['ComercioPage']



# Modelo Página Alimentación
class ComercioPage(Page):

    descripcion = models.CharField(blank=True, max_length=200)
    coord = models.CharField(blank=True, max_length=20)
    categories = ParentalManyToManyField('comercios.ComercioCategory', blank=True)
    imagen = models.URLField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('descripcion'),
    ]

    content_panels = Page.content_panels + [
           
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            
        FieldPanel('coord'),
        FieldPanel('imagen'),
        FieldPanel('descripcion', classname="full"),

    ]


## Modelo para comercios
@register_snippet # Registrado como snippet
class Comercio(models.Model):
    name = models.CharField('name', max_length=250)
    coord = models.CharField(blank=True, max_length=20)
    description = RichTextField(blank=True)
    url = models.URLField(blank=True)
    image = models.URLField()
    categories = ParentalManyToManyField('comercios.ComercioCategory', blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('coord'),
        FieldPanel('description'),
        FieldPanel('url'),
        FieldPanel('image'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]

    def __str__(self):
        return f'{self.name}'



## Modelo para productos
@register_snippet # Registrado como snippet
class Producto(models.Model):
    name = models.CharField('name', max_length=250)
    url = models.URLField(blank=True)
    description = models.CharField(max_length=1000, blank=True)
    image = models.URLField()
    price = models.CharField(max_length=30, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('url'),
        FieldPanel('image'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return f'{self.name} ({self.price}€)'




@register_snippet
class ComercioCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categorías de comercio'
        verbose_name = 'categoría de comercio'