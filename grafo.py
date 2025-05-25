import math

class Grafo:
    def __init__(self):
        self.ciudades = []  # Lista de nombres de ciudades
        self.indices = {}   # Mapa ciudad -> índice
        self.matriz_tiempos = []  # Lista de matrices por clima: normal, lluvia, nieve, tormenta

    def cargar_desde_archivo(self, nombre_archivo):
        self.ciudades = []
        self.indices = {}
        conexiones = []

        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split()
                if len(partes) != 6:
                    continue
                c1, c2 = partes[0], partes[1]
                tiempos = list(map(float, partes[2:]))
                conexiones.append((c1, c2, tiempos))
                if c1 not in self.ciudades:
                    self.ciudades.append(c1)
                if c2 not in self.ciudades:
                    self.ciudades.append(c2)

        self.ciudades.sort()
        self.indices = {ciudad: i for i, ciudad in enumerate(self.ciudades)}
        n = len(self.ciudades)
        self.matriz_tiempos = [
            [[math.inf] * n for _ in range(n)] for _ in range(4)
        ]

        for clima in range(4):
            for i in range(n):
                self.matriz_tiempos[clima][i][i] = 0

        for c1, c2, tiempos in conexiones:
            i = self.indices[c1]
            j = self.indices[c2]
            for clima in range(4):
                self.matriz_tiempos[clima][i][j] = tiempos[clima]

    def obtener_matriz(self, clima):
        clima_indices = {"normal": 0, "lluvia": 1, "nieve": 2, "tormenta": 3}
        return self.matriz_tiempos[clima_indices[clima]]
    
    def eliminar_arco(self, ciudad1, ciudad2):
        if ciudad1 in self.indices and ciudad2 in self.indices:
            i = self.indices[ciudad1]
            j = self.indices[ciudad2]
            for clima in range(4):
                self.matriz_tiempos[clima][i][j] = math.inf