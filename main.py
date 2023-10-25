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
print(calcular_similaridad_coseno(texto_final[0], texto_final[1]))