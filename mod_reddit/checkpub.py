import praw
import requests
from bs4 import BeautifulSoup

    #cargar datos para autenticacion
with open('llaves.txt','r') as f: #actualizar llave
    cliente_id = f.readline()
    cliente_secret = f.readline()
    cliente_id = cliente_id.strip()

    # Configuración de la cuenta de Reddit
reddit = praw.Reddit(client_id=cliente_id,
                     client_secret=cliente_secret,
                     user_agent='python:praw:v1.0 (by /u/Misayeon_29)',
)
# Seleccionar la publicación

subredit = input('Ingrese el subreddit')

for post in reddit.subreddit(subredit).search('hanni',sort='top',time_filter='all',limit=200):
    print(post.title)
    print(post.url)
    #Obtener el título y el enlace de la publicación
    
#for post in reddit.subreddit(subredit).new(limit=40):
 #   print(post.title)
  #  print(post.url)