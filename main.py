import math
import argparse
from funciones.funciones import *

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(
    description='Procesar archivos de entrada y salida.')

# Agregar argumentos de línea de comandos
parser.add_argument('-d', '--doc', type=str, required=True,
                    help='Nombre del archivo con los documentos')
parser.add_argument('-p', '--par', type=str, required=True,
                    help='Nombre del archivo de palabras de parada')
parser.add_argument('-l', '--lem', type=str, required=True,
                    help='Nombre del archivo de lematización')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='Nombre del archivo de salida')


# Analizar los argumentos
args = parser.parse_args()

# Acceder a los nombres de archivo proporcionados
nombre_archivo_documentos = args.doc
nombre_archivo_palabras_parada = args.par
nombre_archivo_lematizacion = args.lem
nombre_archivo_salida = args.output

palabras = leer_archivo_palabras_parada(nombre_archivo_palabras_parada)
texto_inicial = leer_texto(nombre_archivo_documentos)
texto = eliminar_palabras_parada(texto_inicial, palabras)
lematizacion = leer_archivo_lematizacion(nombre_archivo_lematizacion)
texto_final = cambiar_palabras(texto, lematizacion)

array_tablas = []

with open(nombre_archivo_salida, 'w') as archivo:
    # Imprimir las tablas de frecuencia de términos
    for i in range(len(texto_final)):
        archivo.write('Documento ' + str(i + 1) + "\n")
        tabla = crear_tabla(texto_final, texto_final[i])
        archivo.write("Índice del término\tTérmino\tTF\tIDF\tTF-IDF \n")
        for i in range(len(tabla)):
            archivo.write(str(tabla[i][0]) + "\t" + str(tabla[i][1]) + "\t" + str(round(
                tabla[i][2], 5)) + "\t" + str(round(tabla[i][3], 5)) + "\t" + str(round(tabla[i][4], 5)) + "\n")
        archivo.write("\n")
        array_tablas.append(ordenar_mejores_idf(tabla))

    # Imprimir la similitud coseno entre las tablas
    archivo.write('Similitud coseno entre los documentos \n')
    for i in range(len(array_tablas)):
        for j in range(i + 1, len(array_tablas)):
            archivo.write('Similitud coseno entre el documento ' + str(i + 1) + ' y el documento ' + str(
                j + 1) + ': ' + str(round(calcular_similitud_coseno(array_tablas[i], array_tablas[j]), 5)) + '\n')
