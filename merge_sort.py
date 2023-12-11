import time
import os

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

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
carpeta_resultados = "py_resultados_merge_sort"
if not os.path.exists(carpeta_resultados):
    os.makedirs(carpeta_resultados)

# Ejecutar y guardar tiempos para Bubble Sort
ejecutar_y_guardar_tiempos(merge_sort, carpeta_entrada, carpeta_resultados, 5)