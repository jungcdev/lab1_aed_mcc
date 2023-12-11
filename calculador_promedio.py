import os
import math

def calcular_promedio(valores):
    return sum(valores) / len(valores) if len(valores) > 0 else 0

def calcular_desviacion_estandar(datos):
    media = calcular_promedio(datos)
    n= len(datos)
    sum_cuadrados = sum((x - media) ** 2 for x in datos)
    desviacion_estandar = math.sqrt(sum_cuadrados / (n - 1))
    return desviacion_estandar


# Directorio donde se encuentran los archivos
directorio = "go_resultados_insertion_sort"

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Diccionario para almacenar los datos por cada cantidad
datos_por_cantidad = {}

# Iterar sobre cada archivo
for archivo in archivos:
    # Obtener la cantidad desde el nombre del archivo
    cantidad = int(archivo.split('_')[2].split('.')[0])
    
    # Leer los datos del archivo
    ruta_archivo = os.path.join(directorio, archivo)
    with open(ruta_archivo, 'r') as f:
        datos = [float(line.split()[1]) for line in f.readlines()]
    
    # Almacenar los datos en el diccionario
    if cantidad in datos_por_cantidad:
        datos_por_cantidad[cantidad].extend(datos)
    else:
        datos_por_cantidad[cantidad] = datos

# Calcular promedio y desviación estándar para cada cantidad
resultados = []
for cantidad, valores in datos_por_cantidad.items():
    # Calcular promedio
    promedio = calcular_promedio(valores)
    
    # Calcular desviación estándar
    desviacion_estandar = calcular_desviacion_estandar(valores)
    
    resultados.append((cantidad, promedio, desviacion_estandar))

# Generar el archivo de resultados
with open("go_promedio_insertion_sort.txt", 'w') as f:
    for resultado in resultados:
        f.write("{} {} {}\n".format(resultado[0], resultado[1], resultado[2]))