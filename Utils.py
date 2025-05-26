
def mostrar_menu():
    # Muestra el menú principal de opciones al usuario
    print("\n--- Menú de opciones ---")
    print("1. Ruta más corta entre dos ciudades")
    print("2. Ciudad en el centro del grafo")
    print("3. Modificar el grafo")
    print("4. Salir")
    # Solicita y retorna la opción seleccionada por el usuario
    return input("Seleccione una opción: ")

def mostrar_ruta(origen, destino, distancias, rutas, ciudades):
    # Crea un diccionario para mapear nombres de ciudades a sus índices
    indices = {nombre: i for i, nombre in enumerate(ciudades)}

    # Verifica que ambas ciudades existan en el grafo
    if origen not in indices or destino not in indices:
        print("Una o ambas ciudades no existen.")
        return

    i = indices[origen]
    j = indices[destino]

    # Si no hay ruta posible, informa al usuario
    if distancias[i][j] == float('inf'):
        print("No hay ruta entre las ciudades.")
    else:
        # Muestra el tiempo mínimo y la ruta óptima
        print(f"Tiempo mínimo: {distancias[i][j]} horas")
        ruta = rutas[i][j]
        nombres = [ciudades[k] for k in ruta]
        print("Ruta: " + " -> ".join(nombres))