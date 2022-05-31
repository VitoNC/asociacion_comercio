from comercios.models import Producto
import json
import os

# borrar productos
for p in Producto.objects.all():
    p.delete()

#lista de productos del json
if os.path.exists("datos/comercios/general/prod_data.json"):
    productos = json.load(open("datos/comercios/general/prod_data.json"))
else:
    productos = json.load(open("datos/comercios/general/prod_data.json"))

'''
{
        "img": "https://www.pradojaca.es/500-home_default/jabon-de-alepo-certificado-cosmos-natura.jpg",
        "url": "https://www.pradojaca.es/cuidado-corporal/249-jabon-de-alepo-certificado-cosmos-natura-3593290030071.html",
        "name": "Jabón De Alepo Certificado...",
        "price": "4.7",
        "description": " 100 gr. Jabón de Alepo certificado Cosmos en Siria "
    }
'''


for p1 in productos:
    p = Producto()
    p.name = p1["name"]
    p.description = p1["description"]
    p.url = p1["url"]
    p.image = p1["img"]
    p.price = p1["price"]

    p.save()