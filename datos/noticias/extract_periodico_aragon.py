
import requests
from lxml import html
from urllib.parse import urljoin
import json

headers = {"Accept-Language": "es-es,es;q=0.5"}




def noticias_data(noticia):

    data = {}

    elementos = noticia.xpath(".//a")
    image = elementos[0]
    seccion = elementos[1]
    # titulo = elementos[2]



    #imagen
    image_src = image.xpath("./picture/@src")
    data['img'] = image_src

    # url
    url = image.xpath("./@href")[0]
    data['url'] = url


    # nombre
    title = image.xpath("./@title")[0]
    data['title'] = title

    # sección
    topic = seccion.xpath("./span/text()")[0]
    data['topic'] = topic


    # data.update(detalle(url))

    return data

if __name__ == '__main__':

    url = 'https://www.elperiodicodearagon.com/aragon/jaca/'

    response = requests.get(url, headers=headers)
    pagina = html.fromstring(response.text)

    # noticias_header = pagina.xpath("//article[@data-bbnx-id='5968c5bc-cdf9-4170-8bb3-121ceb60c38f']")
    noticias_body = (pagina.xpath("//article[@class='lst ']") + pagina.xpath("//article[@class='lst  premium']"))



    data = [noticias_data(n) for n in noticias_body]
    # data = [prod_data(n) for n in noticias_body]

    json.dump(data, open('noticia_data.json', 'w'))



# Automatizar Autenticación en sitios Web


# sesion = requests.session()

#urllogin = 'http://localhost:8000/admin/login/'

#datos = {}
#datos['username'] = 'usuario'
#datos['password'] = 'contraseña'


#respuesta = sesion.get(url)

#doc = html.fromstring(respuesta.content)

#datos['csrfmiddlewaretoken'] = doc.xpath("//input[@name='csrfmiddlewaretoken']/value")

#resp = sesion.post(urllogin, data = datos)