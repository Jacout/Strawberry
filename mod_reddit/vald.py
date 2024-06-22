import praw

def cargar():
    #cargar datos para autenticacion
    with open('llaves.txt','r') as f:
        cliente_id = f.readline()
        cliente_secret = f.readline()
        cliente_id = cliente_id.strip()

    # Configuración de la cuenta de Reddit
    reddit = praw.Reddit(client_id=cliente_id,
                     client_secret=cliente_secret,
                     user_agent='python:praw:v1.0 (by /u/Misayeon_29)',
)
    return reddit