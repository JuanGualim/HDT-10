# floyd.py
import math
import copy

def floyd_warshall(grafo, clima):
    matriz = copy.deepcopy(grafo.obtener_matriz(clima))
    n = len(grafo.ciudades)
    rutas = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] != math.inf:
                rutas[i][j] = [i, j]
            elif i == j:
                rutas[i][j] = [i]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matriz[i][k] + matriz[k][j] < matriz[i][j]:
                    matriz[i][j] = matriz[i][k] + matriz[k][j]
                    rutas[i][j] = rutas[i][k][:-1] + rutas[k][j]

    return matriz, rutas

def calcular_centro(distancias, ciudades):
    n = len(ciudades)
    excentricidades = [max([distancias[i][j] for j in range(n) if i != j]) for i in range(n)]
    min_excentricidad = min(excentricidades)
    centro_idx = excentricidades.index(min_excentricidad)
    return ciudades[centro_idx]
