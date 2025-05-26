# utils.py
def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Ruta más corta entre dos ciudades")
    print("2. Ciudad en el centro del grafo")
    print("3. Modificar el grafo")
    print("4. Salir")
    return input("Seleccione una opción: ")

def mostrar_ruta(origen, destino, distancias, rutas, ciudades):
    indices = {nombre: i for i, nombre in enumerate(ciudades)}

    if origen not in indices or destino not in indices:
        print("Una o ambas ciudades no existen.")
        return

    i = indices[origen]
    j = indices[destino]

    if distancias[i][j] == float('inf'):
        print("No hay ruta entre las ciudades.")
    else:
        print(f"Tiempo mínimo: {distancias[i][j]} horas")
        ruta = rutas[i][j]
        nombres = [ciudades[k] for k in ruta]
        print("Ruta: " + " -> ".join(nombres))
