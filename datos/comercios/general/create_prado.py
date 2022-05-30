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


for p1 in productos:
    p = Producto()
    p.name = p1["name"]
    p.description = p1["description"]
    p.url = p1["url"]
    p.image = p1["image"]
    p.price = p1["price"]

    p.save()