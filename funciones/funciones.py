import json
import re

# Función que lee las palabras de parada de un archivo
def leer_archivo_palabras_parada(nombre_archivo_palabras_parada):
    with open(nombre_archivo_palabras_parada, 'r') as archivo:
        lineas = archivo.readlines()
        palabras = []
        for lineas in lineas:
            palabras.append(lineas.strip())
    return palabras

# Función que lee el texto
def leer_texto(nombre_archivo_documentos):
    # Inicializa un vector vacío para almacenar los vectores de palabras
    vector_de_lineas = []

    # Abre el archivo y lee línea por línea
    with open(nombre_archivo_documentos, 'r') as archivo:
        for linea in archivo:
            # Divide la línea en palabras
            palabras = linea.split()
            # Agrega el vector de palabras al vector principal
            vector_de_lineas.append(palabras)

    return vector_de_lineas

# Función que elimina las palabras de parada de un texto
def eliminar_palabras_parada(texto, palabras):
    for i in palabras:
        for j in texto:
            for k in j:
                if i == k:
                    j.remove(k)
    return texto

# Función que lee el archivo lematización
def leer_archivo_lematizacion(nombre_archivo_lematizacion):
    with open(nombre_archivo_lematizacion, 'r') as archivo:
        texto = archivo.read()
        texto_json = json.loads(texto)
    return texto_json

# Función que cambia las palabras por otras dadas
def cambiar_palabras(texto, lematizacion):
    for palabra_original, palabra_lematizada in lematizacion.items():
        for i in range(len(texto)):
            for j in range(len(texto[i])):
                if texto[i][j] == palabra_original:
                    texto[i][j] = palabra_lematizada
    return texto

    


