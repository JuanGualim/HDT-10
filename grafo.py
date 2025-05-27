import math

class Grafo:
    def __init__(self):
        # Lista de nombres de ciudades en el grafo
        self.ciudades = []
        # Diccionario que mapea el nombre de la ciudad a su índice en la matriz
        self.indices = {}
        # Lista de 4 matrices de adyacencia, una por cada clima (normal, lluvia, nieve, tormenta)
        self.matriz_tiempos = []

    def cargar_desde_archivo(self, nombre_archivo):
        """
        Carga el grafo desde un archivo de texto.
        Cada línea debe tener: ciudad1 ciudad2 tiempo_normal tiempo_lluvia tiempo_nieve tiempo_tormenta
        """
        self.ciudades = []
        self.indices = {}
        conexiones = []

        # Leer el archivo línea por línea
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split()
                if len(partes) != 6:
                    continue  # Ignora líneas mal formateadas
                c1, c2 = partes[0], partes[1]
                tiempos = list(map(float, partes[2:]))
                conexiones.append((c1, c2, tiempos))
                # Agrega las ciudades si no existen
                if c1 not in self.ciudades:
                    self.ciudades.append(c1)
                if c2 not in self.ciudades:
                    self.ciudades.append(c2)

        # Ordena las ciudades y crea el índice
        self.ciudades.sort()
        self.indices = {ciudad: i for i, ciudad in enumerate(self.ciudades)}
        n = len(self.ciudades)
        # Inicializa las matrices de adyacencia para cada clima
        self.matriz_tiempos = [
            [[math.inf] * n for _ in range(n)] for _ in range(4)
        ]

        # El tiempo de una ciudad a sí misma es 0
        for clima in range(4):
            for i in range(n):
                self.matriz_tiempos[clima][i][i] = 0

        # Llena las matrices con los tiempos leídos
        for c1, c2, tiempos in conexiones:
            i = self.indices[c1]
            j = self.indices[c2]
            for clima in range(4):
                self.matriz_tiempos[clima][i][j] = tiempos[clima]

    def obtener_matriz(self, clima):
        """
        Devuelve la matriz de adyacencia correspondiente al clima dado.
        clima: "normal", "lluvia", "nieve" o "tormenta"
        """
        clima_indices = {"normal": 0, "lluvia": 1, "nieve": 2, "tormenta": 3}
        return self.matriz_tiempos[clima_indices[clima]]
    
    def agregar_arco(self, ciudad1, ciudad2, tiempos):
        """
        Agrega un arco entre ciudad1 y ciudad2 con los tiempos dados para cada clima.
        tiempos: lista de 4 valores (uno por clima)
        """
        # Asegura que ambas ciudades estén en la lista
        for ciudad in [ciudad1, ciudad2]:
            if ciudad not in self.ciudades:
                self.ciudades.append(ciudad)
        self.ciudades.sort()
        self.indices = {ciudad: i for i, ciudad in enumerate(self.ciudades)}
        n = len(self.ciudades)

        # Expande las matrices si hay nuevas ciudades
        while len(self.matriz_tiempos[0]) < n:
            for clima in range(4):
                for fila in self.matriz_tiempos[clima]:
                    fila.append(math.inf)
                self.matriz_tiempos[clima].append([math.inf] * n)

        # El tiempo de una ciudad a sí misma es 0
        for clima in range(4):
            for i in range(n):
                self.matriz_tiempos[clima][i][i] = 0

        # Asigna los tiempos al arco correspondiente
        i = self.indices[ciudad1]
        j = self.indices[ciudad2]
        for clima in range(4):
            self.matriz_tiempos[clima][i][j] = tiempos[clima]

    def eliminar_arco(self, ciudad1, ciudad2):
        """
        Elimina el arco de ciudad1 a ciudad2 (lo pone como infinito en todas las matrices).
        """
        if ciudad1 in self.indices and ciudad2 in self.indices:
            i = self.indices[ciudad1]
            j = self.indices[ciudad2]
            for clima in range(4):
                self.matriz_tiempos[clima][i][j] = math.inf
    
    def guardar_en_archivo(self, nombre_archivo):
        """
        Guarda el grafo actual en un archivo de texto, en el mismo formato que cargar_desde_archivo.
        """
        with open(nombre_archivo, "w") as archivo:
            n = len(self.ciudades)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        tiempos = [self.matriz_tiempos[k][i][j] for k in range(4)]
                        # Solo guarda los arcos existentes (no infinitos)
                        if all(t != float('inf') for t in tiempos):
                            linea = f"{self.ciudades[i]} {self.ciudades[j]} {' '.join(map(str, tiempos))}\n"
                            archivo.write(linea)
                            
