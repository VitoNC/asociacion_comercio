
import requests
from lxml import html
from urllib.parse import urljoin
import json

headers = {"Accept-Language": "es-es,es;q=0.5"}






def prod_data(prod):

    data = {}

    elementos = prod.xpath(".//div")
    image = elementos[0]
    meta = elementos[5]
    description = elementos[7]



    #imagen
    image_src = image.xpath(".//a/img/@src")[0]
    data['img'] = image_src

    # url
    url = image.xpath(".//a/@href")[0]
    data['url'] = url


    # nombre
    name = meta.xpath(".//h3/a/text()")[0]
    data['name'] = name

    # price
    price = meta.xpath(".//span[@itemprop='price']/@content")[0]
    data['price'] = price


    # description
    descripcion = description.xpath(".//text()")[0]
    data['description'] = descripcion


    
    # data.update(detalle(url))

    return data

if __name__ == '__main__':

    url = 'https://www.pradojaca.es/'

    response = requests.get(url, headers=headers)
    pagina = html.fromstring(response.text)

    productos = pagina.xpath("//div[@class='thumbnail-container']")


    data = [prod_data(p) for p in productos]
    json.dump(data, open('prod_data.json', 'w'))



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