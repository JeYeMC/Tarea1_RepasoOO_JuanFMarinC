import os

def contar_palabra_en_archivos(ruta_carpeta, palabra):
    total_ocurrencias = 0
    archivos_encontrados = False

    # Lista de extensiones de archivos de texto permitidas
    extensiones_permitidas = ['.txt', '.xml', '.json', '.csv']

    # Verificar si la carpeta existe
    if not os.path.exists(ruta_carpeta):
        print("La carpeta especificada no existe.")
        return

    # Recorre todos los archivos en la carpeta
    for archivo in os.listdir(ruta_carpeta):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        # Verifica si el archivo es de texto y tiene una extensión permitida
        if os.path.isfile(ruta_archivo) and archivo.endswith(tuple(extensiones_permitidas)):
            archivos_encontrados = True
            # Lee el contenido del archivo
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                # Cuenta la cantidad de veces que aparece la palabra en el contenido
                ocurrencias = contenido.lower().count(palabra.lower())
                total_ocurrencias += ocurrencias
                # Muestra la cantidad de veces que está la palabra en el archivo
                print("Archivo '{}': {} veces".format(archivo, ocurrencias))

    if not archivos_encontrados:
        print("No se encontraron archivos de texto en la carpeta.")
        return

    # Muestra la cantidad total de ocurrencias en toda la carpeta
    print("\nTotal de ocurrencias de la palabra '{}' en la carpeta: {}".format(palabra, total_ocurrencias))

# Prueba 1
print("Prueba 1:")
contar_palabra_en_archivos("C:/Users/felipe/Desktop/Software/pruebas1", "arar")
print("\n")

# Prueba 2
print("Prueba 2:")
contar_palabra_en_archivos("C:/Users/felipe/Desktop/Software/pruebas2", "foto")
print("\n")

# Prueba 3
print("Prueba 3:")
contar_palabra_en_archivos("C:/Users/felipe/Desktop/Software/pruebas3", "ejemplo")
print("\n")
