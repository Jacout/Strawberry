import os

def eliminar_archivos_no_imagenes(directorio):
    print(directorio)
    for nombre_archivo in os.listdir(directorio):
        if not nombre_archivo.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif','.mp4')):
            ruta_archivo = os.path.join(directorio, nombre_archivo)
            try:
                if os.path.isfile(ruta_archivo) or os.path.islink(ruta_archivo):
                    os.unlink(ruta_archivo)
                    print(f'Se eliminó con éxito {ruta_archivo}')
            except Exception as e:
                print(f'Error al eliminar {ruta_archivo}. Razón: {e}')

# uso
directorio = input("Directorio")
eliminar_archivos_no_imagenes(directorio) #nomas ingresas el nombre de la ruta