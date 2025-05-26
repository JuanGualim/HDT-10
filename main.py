# main.py
from Grafo import Grafo
from Floyd import floyd_warshall, calcular_centro
from Utils import mostrar_menu, mostrar_ruta

# Cargar grafo desde archivo
grafo = Grafo()
grafo.cargar_desde_archivo("logistica.txt")

# Estado del clima actual
clima_actual = "normal"

# Ejecutar algoritmo de Floyd inicialmente
distancias, rutas = floyd_warshall(grafo, clima_actual)
terminar = False
while terminar == False:
    opcion = mostrar_menu()

    if opcion == "1":
        origen = input("Ciudad origen: ")
        destino = input("Ciudad destino: ")
        if origen in grafo.ciudades and destino in grafo.ciudades:
            mostrar_ruta(origen, destino, distancias, rutas, grafo.ciudades)
        else:
            print("Una de las ciudades no existe en el grafo.")

    elif opcion == "2":
        centro = calcular_centro(distancias, grafo.ciudades)
        print(f"La ciudad en el centro del grafo es: {centro}")

    elif opcion == "3":
        print("1. Interrupción entre ciudades")
        print("2. Agregar conexión")
        print("3. Cambiar clima")
        subop = input("Seleccione una opción: ")

        if subop == "1":
            c1 = input("Ciudad origen: ")
            c2 = input("Ciudad destino: ")
            grafo.eliminar_arco(c1, c2)

        elif subop == "2":
            c1 = input("Ciudad origen: ")
            c2 = input("Ciudad destino: ")
            tiempos = input("Ingrese los tiempos para cada clima: normal, lluvia, nieve, tormenta. Separados por espacio: ").split()
            tiempos = list(map(float, tiempos))
            grafo.agregar_arco(c1, c2, tiempos)

        elif subop == "3":
            nuevo_clima = input("Ingrese clima (normal, lluvia, nieve, tormenta): ")
            if nuevo_clima in ["normal", "lluvia", "nieve", "tormenta"]:
                clima_actual = nuevo_clima
                print(f"Clima actualizado a {clima_actual}")
            else:
                print("Clima inválido")

        distancias, rutas = floyd_warshall(grafo, clima_actual)

    elif opcion == "4":
        print("Saliendo del programa...")
        terminar = True

    else:
        print("Opción inválida")
