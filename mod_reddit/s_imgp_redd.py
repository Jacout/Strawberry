import praw
import requests
from PIL import Image
from io import BytesIO
import os

#cargar datos para autenticacion
with open('mod_reddit/llaves.txt','r') as f: #poner ruta aqui de tu llave
    cliente_id = f.readline()
    cliente_secret = f.readline()
    cliente_id = cliente_id.strip()

# Configuración de la cuenta de Reddit
reddit = praw.Reddit(client_id=cliente_id,
                     client_secret=cliente_secret,
                     user_agent='python:praw:v1.0 (by /u/Misayeon_29)',
)

# Ingresar el subreddit
subreddit = input('ingrese el subreddit ')

# Set up the image directory
image_dir = subreddit

# Create the image directory if it doesn't exist
if not os.path.exists(image_dir):
    os.makedirs(image_dir)
    
# Obtener el subreddit
sub = reddit.subreddit(subreddit)

# Loop through each post
for post in sub.hot(limit=50):
    print(post.url)
    # Check if the post is an image
    if post.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Download the image
        response = requests.get(post.url)
        image = Image.open(BytesIO(response.content))
        # Save the image
        image.save(os.path.join(image_dir, post.id + '.' + image.format))
    # Check if the post is a carousel galeria comunmente
    if post.url.startswith('https://www.reddit.com/gallery/'):
        # Get the carousel media
        media = post.media_metadata
        # Loop through each image in the carousel
        for key, value in media.items():
            # Download the image
            response = requests.get(value['s']['u'])
            image = Image.open(BytesIO(response.content))
            # Save the image
            image.save(os.path.join(image_dir, post.id + '_' + key + '.' + image.format))
            image.close()