from urllib.request import urlopen #herramienta para abrir la pag web
from bs4 import BeautifulSoup #para extraer la informacion
    
url = 'https://www.vans.cl/calzado/Mujer?PS=12&map=c,specificationFilter_39&O=OrderByReleaseDateDESC'


#pasos para abrir la pagina y extraer informacion, es como un permiso 
request_page = urlopen(url)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')
                         

#aqui empece a llamar a la informacion que necesito con los div en su codigo html
zapatillas = html_soup.find_all('div', class_='product-block')
#este de arriba es el anuncio dentro de la pag web
for calzado in zapatillas:
    titulo = html_soup.find_all('div', class_='productName')
    precio = html_soup.find_all('div', class_='product-block-price')
    
#este for es para extraer la info dentro de ese anuncion, su titulo(lo que es) y su precio 

