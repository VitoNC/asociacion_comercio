'''
crear noticias

ejecutar:

python manage.py shell < datos/noticias/create_noticias.py
'''

from noticias.models import Noticia
import json
import os


# borrar noticias
for n in Noticia.objects.all():
    n.delete()

#lista de noticias del json
if os.path.exists("datos/noticias/noticia_data.json"):
    noticias = json.load(open("datos/noticias/noticia_data.json"))
elif os.path.exists("noticias/noticia.json"):
    noticias = json.load(open("noticias/noticia_data.json"))
else:
    noticias = json.load(open("noticia_data.json"))


'''
{
        "img": "https://estaticos-cdn.prensaiberica.es/clip/d179498f-1751-40ae-8cbd-a8b4837ac564_16-9-aspect-ratio_default_0.jpg",
        "url": "/cultura/2022/05/25/20-conciertos-exposiciones-actividades-paralelas-66516579.html",
        "title": "Más de 20 conciertos, exposiciones y actividades paralelas conforman el Festival En el Camino de Santiago",
        "topic": "Cultura"
    }
'''

for n1 in noticias:
    print(n1)
    n = Noticia()
    n.title = n1["title"]
    n.imagen = n1["img"]
    n.topic = n1["topic"]
    n.url = "https://www.elperiodicodearagon.com/aragon/" + n1["url"]

    n.save()

