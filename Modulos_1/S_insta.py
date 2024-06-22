import instaloader, time

def descargar_medios_de_instagram(usuario):
    # Instanciar un objeto Instaloader
    L = instaloader.Instaloader()
    
    # Descargar el perfil
    perfil = instaloader.Profile.from_username(L.context, usuario)
    for post in perfil.get_posts():
        L.download_post(post, target='#' + usuario)
        time.sleep(10)
    

# Uso
user = input('Usuario')
descargar_medios_de_instagram(user)