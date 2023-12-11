import matplotlib.pyplot as plt

# Función para leer un archivo y devolver dos listas: tamaños y tiempos
def leer_archivo(nombre_archivo):
    tamanos = []
    tiempos = []
    with open(nombre_archivo, 'r') as file:
        for line in file:
            elementos = line.split()
            tamanos.append(int(elementos[0]))
            tiempos.append(float(elementos[1]))
    return tamanos, tiempos

# Nombres de los archivos
archivos = ['py_promedio_quick_sort.txt', 'go_promedio_quick_sort.txt', 'cpp_promedio_quick_sort.txt']

# Listas para almacenar los datos de cada archivo
datos_tamanos = []
datos_tiempos = []

# Leer cada archivo y almacenar los datos
for archivo in archivos:
    tamanos, tiempos = leer_archivo(archivo)
    datos_tamanos.append(tamanos)
    datos_tiempos.append(tiempos)

# Ordenar los datos por tamaños
for i in range(len(archivos)):
    datos_tamanos[i], datos_tiempos[i] = zip(*sorted(zip(datos_tamanos[i], datos_tiempos[i])))

# Colores y leyendas personalizadas
colores = ['red', 'green', 'blue']
leyendas = ['Python', 'GO', 'C++']

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar cada conjunto de datos con colores y leyendas personalizadas
for i in range(len(archivos)):
    plt.plot(datos_tamanos[i], datos_tiempos[i], label=leyendas[i], color=colores[i], marker = 'o')

# Configuración de la gráfica
plt.title('Comparación de Tiempos de Ejecución  - Quick Sort')
plt.xlabel('Tamaño')
plt.ylabel('Tiempo de Ejecución')
plt.legend()
plt.grid(True)

plt.savefig("quick_sort.png")
# Mostrar la gráfica
plt.show()
