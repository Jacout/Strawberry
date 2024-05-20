import instaloader
import time

usuario = input("Ingrese el usuario")
contador = 0
# Inicializa Instaloader
L = instaloader.Instaloader()

# Obtiene el perfil de Instagram
profile = instaloader.Profile.from_username(L.context, usuario)

# Descarga las publicaciones del perfil
for post in profile.get_posts():
    L.download_post(post, target=usuario)
    time.sleep(7)
    contador += 1
    if contador == 10:
        d = int(input("Desea seguir con el proceso?, 1. SI, 2. NO"))
        if d == 1:
            contador = 0
        else:
            break
