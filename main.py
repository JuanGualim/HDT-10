# main.py

from Grafo import Grafo
from Floyd import floyd_warshall, calcular_centro
from Utils import mostrar_menu, mostrar_ruta

# Crea una instancia del grafo y lo carga desde el archivo
grafo = Grafo()
grafo.cargar_desde_archivo("logistica.txt")

# Estado del clima actual (por defecto "normal")
clima_actual = "normal"

# Ejecuta el algoritmo de Floyd-Warshall inicialmente para obtener distancias y rutas
distancias, rutas = floyd_warshall(grafo, clima_actual)

terminar = False
while terminar == False:
    # Muestra el menú principal y obtiene la opción del usuario
    opcion = mostrar_menu()

    if opcion == "1":
        # Opción para mostrar la ruta más corta entre dos ciudades
        origen = input("Ciudad origen: ")
        destino = input("Ciudad destino: ")
        if origen in grafo.ciudades and destino in grafo.ciudades:
            mostrar_ruta(origen, destino, distancias, rutas, grafo.ciudades)
        else:
            print("Una de las ciudades no existe en el grafo.")

    elif opcion == "2":
        # Opción para mostrar la ciudad en el centro del grafo
        centro = calcular_centro(distancias, grafo.ciudades)
        print(f"La ciudad en el centro del grafo es: {centro}")

    elif opcion == "3":
        # Opción para modificar el grafo
        print("1. Interrupción entre ciudades")
        print("2. Agregar conexión")
        print("3. Cambiar clima")
        subop = input("Seleccione una opción: ")

        if subop == "1":
            # Elimina la conexión entre dos ciudades
            c1 = input("Ciudad origen: ")
            c2 = input("Ciudad destino: ")
            grafo.eliminar_arco(c1, c2)

        elif subop == "2":
            # Agrega una nueva conexión entre dos ciudades con los tiempos para cada clima
            c1 = input("Ciudad origen: ")
            c2 = input("Ciudad destino: ")
            tiempos = input("Ingrese los tiempos para cada clima: normal, lluvia, nieve, tormenta. Separados por espacio: ").split()
            tiempos = list(map(float, tiempos))
            grafo.agregar_arco(c1, c2, tiempos)

        elif subop == "3":
            # Cambia el clima actual
            nuevo_clima = input("Ingrese clima (normal, lluvia, nieve, tormenta): ")
            if nuevo_clima in ["normal", "lluvia", "nieve", "tormenta"]:
                clima_actual = nuevo_clima
                print(f"Clima actualizado a {clima_actual}")
            else:
                print("Clima inválido")

        # Después de cualquier cambio, recalcula las distancias y rutas y guarda el grafo
        distancias, rutas = floyd_warshall(grafo, clima_actual)
        grafo.guardar_en_archivo("logistica.txt")

    elif opcion == "4":
        # Opción para salir del programa
        print("Saliendo del programa...")
        terminar = True

    else:
        # Opción inválida
        print("Opción inválida")