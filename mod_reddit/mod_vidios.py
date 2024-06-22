import requests
import praw
import os
import time

def download_video(url, filename):
    response = requests.get(url, stream=True)
    with open(os.path.join(download_folder, filename), "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
            
sub = input('Subreddit a buscar videos ')
download_folder = sub + '_vidios'

#checar si existe si no lo creoa
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    
#cargar datos para autenticacion
with open('llaves.txt','r') as f: #actualizar ruta relativa del archivo de la llave
    cliente_id = f.readline()
    cliente_secret = f.readline()
    cliente_id = cliente_id.strip()

    # Configuración de la cuenta de Reddit
reddit = praw.Reddit(client_id=cliente_id,
                     client_secret=cliente_secret,
                     user_agent='python:praw:v1.0 (by /u/Misayeon_29)',
)

subreddit = reddit.subreddit(sub)
n = 1
for submission in subreddit.search('flair:Hanni',sort ='top',limit=200):  # Descarga los 100 últimos posts
    if submission.is_video:
        try:
            print(submission.media)
            video_url = submission.media["reddit_video"]["fallback_url"]
            filename = f"{submission}n.mp4"
            print(f"Descargando {filename}...")
            download_video(video_url, filename)
            print(f"Descarga completa: {filename}")
            n += 1
            time.sleep(2)
        except Exception as e:
            print(e)
            pass
        
