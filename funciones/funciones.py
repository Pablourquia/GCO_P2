import json
import re
import math

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

            # revisa si en el vector de palabras hay un espacio en blanco o un . o una , y si lo hay, lo elimina
            for i in range(len(palabras)):
                if palabras[i] == ' ' or palabras[i] == '.' or palabras[i] == ',':
                    palabras.pop(i)
            vector_de_lineas.append(palabras)

    # eliminar los caracteres como . o , de las palabras
    for i in range(len(vector_de_lineas)):
        for j in range(len(vector_de_lineas[i])):
            vector_de_lineas[i][j] = re.sub(
                r'[^a-zA-Z0-9]', '', vector_de_lineas[i][j])
            vector_de_lineas[i][j] = vector_de_lineas[i][j].lower()

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

def calcular_vector_length(documento):
    array = []
    for i in documento:
        array.append(calcular_TF(i, documento))
    return math.sqrt(sum(i**2 for i in array))



# Funcion que calcula el TF de un término


def calcular_TF(termino, documento):
    # numero de veces que aparece la palabra en el documento
    tf = 0
    for i in documento:
        if i == termino:
            tf += 1
    return 1 + math.log(tf, 10)


# Funcion que calcula el IDF de un término


def calcular_IDF(termino, documentos):
    df = 0
    for i in documentos:
        for j in i:
            if j == termino:
                df += 1
                break
    return math.log(len(documentos) / df, 10)

# Funcion que calcula el TF-IDF de un término


def calcular_TF_IDF(termino, documento, documentos):
    return calcular_TF(termino, documento) * calcular_IDF(termino, documentos)

# Función que calcula el índice del término


def calcular_indice_termino(termino, documento):
    indice = []
    for i in range(len(documento)):
        if documento[i] == termino:
            indice.append(i)
    return indice


def buscar_palabra(termino, tabla):
    for i in range(len(tabla)):
        if tabla[i][1] == termino:
            return i
    return -1

# Función que para cada documento me va a crear una tabla con:
# Índice del término, término, TF, IDF, TF-IDF


def crear_tabla(documentos, documento):
    tabla = []
    for i in documento:
        if buscar_palabra(i, tabla) == -1:
            array = []
            array.append(calcular_indice_termino(i, documento))
            array.append(i)
            array.append(calcular_TF(i, documento))
            array.append(calcular_IDF(i, documentos))
            array.append(calcular_TF_IDF(i, documento, documentos))
            tabla.append(array)
    return tabla

# Función que ordena las tablas por el IDF y devuelve los 5 mejores


def ordenar_mejores_idf(tabla):
    tabla.sort(key=lambda x: x[4], reverse=True)
    return tabla[:5]

# Calcula la similitud coseno entre varias tablas


def calcular_similitud_coseno(tabla1, tabla2, documento1, documento2):
    similitud = 0
    if len(tabla1) != len(tabla2):
        return -1
    for i in range(len(tabla1)):
        similitud += (tabla1[i][4]/calcular_vector_length(documento1)) * (tabla2[i][4]/calcular_vector_length(documento2))
    return similitud