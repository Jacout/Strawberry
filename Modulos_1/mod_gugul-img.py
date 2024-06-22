import os
from google_images_download import google_images_download

# Definimos la búsqueda y el número de imágenes a descargar
search_params = {
    'keywords': 'Zhou Xinyu',
    'count': 10
}

# Ejecutamos la búsqueda y descargamos las imágenes
response = google_images_download.googleimagesdownload()
paths = response.download(search_params)
print(paths)