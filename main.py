import math
import argparse

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

