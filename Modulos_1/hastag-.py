import instaloader, time

# Inicializa Instaloader
L = instaloader.Instaloader()

# Define el hashtag que quieres descargar
hashtag1 = 'KPOP'

# Obtiene las publicaciones del hashtag

# Descarga las publicaciones del hashtag
contador = 0
for post in instaloader.Hashtag.from_name(L.context, 'cat').get_posts():
    L.download_post(post, target='#cat')
    time.sleep(7)
    contador += 1
    if contador == 10:
        d = int(input("Desea seguir con el proceso?, 1. SI, 2. NO"))
        if d == 1:
            contador = 0
        else:
            break
        
    