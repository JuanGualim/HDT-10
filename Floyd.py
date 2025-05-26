import math
import copy

def floyd_warshall(grafo, clima):
    """
    Implementa el algoritmo de Floyd-Warshall para encontrar los caminos más cortos entre todas las parejas de nodos.
    También reconstruye las rutas óptimas.
    Parámetros:
        grafo: instancia de la clase Grafo
        clima: string que indica el clima ("normal", "lluvia", "nieve", "tormenta")
    Retorna:
        matriz: matriz de distancias mínimas entre cada par de ciudades
        rutas: matriz con las rutas óptimas (listas de índices de ciudades)
    """
    # Copia la matriz de adyacencia para no modificar la original
    matriz = copy.deepcopy(grafo.obtener_matriz(clima))
    n = len(grafo.ciudades)
    # Inicializa la matriz de rutas
    rutas = [[[] for _ in range(n)] for _ in range(n)]

    # Inicializa las rutas directas
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] != math.inf:
                rutas[i][j] = [i, j]  # Ruta directa
            elif i == j:
                rutas[i][j] = [i]     # Ruta a sí mismo

    # Algoritmo principal de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Si el camino pasando por k es más corto, actualiza la distancia y la ruta
                if matriz[i][k] + matriz[k][j] < matriz[i][j]:
                    matriz[i][j] = matriz[i][k] + matriz[k][j]
                    rutas[i][j] = rutas[i][k][:-1] + rutas[k][j]

    return matriz, rutas

def calcular_centro(distancias, ciudades):
    """
    Calcula el centro del grafo, es decir, la ciudad cuya excentricidad es mínima.
    Parámetros:
        distancias: matriz de distancias mínimas entre ciudades
        ciudades: lista de nombres de ciudades
    Retorna:
        El nombre de la ciudad que es el centro del grafo.
    """
    n = len(ciudades)
    # Calcula la excentricidad de cada ciudad (la mayor distancia a cualquier otra ciudad)
    excentricidades = [max([distancias[i][j] for j in range(n) if i != j]) for i in range(n)]
    min_excentricidad = min(excentricidades)
    centro_idx = excentricidades.index(min_excentricidad)
    return ciudades[centro_idx]