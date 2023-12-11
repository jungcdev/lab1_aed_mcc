import time
import os

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def medir_tiempo(algoritmo, datos):
    inicio = time.time()
    algoritmo(datos)
    fin = time.time()
    return fin - inicio

def leer_lista_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lista = [int(line.strip()) for line in archivo]
    return lista

def ejecutar_y_guardar_tiempos(algoritmo, carpeta_entrada, carpeta_salida, repeticiones):
    archivos_txt = [f for f in os.listdir(carpeta_entrada) if f.endswith(".txt")]

    for archivo_txt in archivos_txt:
        ruta_entrada = os.path.join(carpeta_entrada, archivo_txt)
        tiempos = []
        datos = leer_lista_desde_archivo(ruta_entrada)
        for _ in range(repeticiones):
            tiempo = medir_tiempo(algoritmo, datos.copy())
            tiempos.append(tiempo)

        nombre_salida = "time_" + archivo_txt.replace('.txt', '') + ".txt"
        ruta_salida = os.path.join(carpeta_salida, nombre_salida)

        with open(ruta_salida, 'w') as archivo_salida:
            for tiempo in tiempos:
                archivo_salida.write(str(len(datos)) + " {:.10f}\n".format(tiempo))

# Carpeta de entrada que contiene los archivos de texto
carpeta_entrada = "numeros_aleatorios"

# Crear una carpeta para almacenar los resultados
carpeta_resultados = "py_resultados_bubble_sort"
if not os.path.exists(carpeta_resultados):
    os.makedirs(carpeta_resultados)

# Ejecutar y guardar tiempos para Bubble Sort
ejecutar_y_guardar_tiempos(bubble_sort, carpeta_entrada, carpeta_resultados, 5)