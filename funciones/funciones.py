import json

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
    with open(nombre_archivo_documentos, 'r') as archivo:
        lineas = archivo.readlines()
        texto = []
        for linea in lineas:
            texto.append(linea)
    return texto

# Función que elimina las palabras de parada de un texto
def eliminar_palabras_parada(texto, palabras):
    for i in palabras:
        for j in range(len(texto)):
            texto[j] = texto[j].replace(i, '')
    return texto

# Función que lee el archivo lematización
def leer_archivo_lematizacion(nombre_archivo_lematizacion):
    with open(nombre_archivo_lematizacion, 'r') as archivo:
        texto = archivo.read()
        texto_json = json.loads(texto)
    return texto_json

# Función que cambia las palabras por otras dadas
def cambiar_palabras(texto, lematizacion):
    for i in lematizacion: # Falla en este bucle
        for j in range(len(texto)):
            texto[j] = texto[j].replace(i, lematizacion[i])
    return texto
