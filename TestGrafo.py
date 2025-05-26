# tests/test_grafo.py
import unittest
import math
from Grafo import Grafo
from Floyd import floyd_warshall, calcular_centro

class TestGrafo(unittest.TestCase):
    def setUp(self):
        self.grafo = Grafo()
        with open("logistica_test.txt", "w") as f:
            f.write("CiudadA CiudadB 10 15 20 25\n")
            f.write("CiudadB CiudadC 5 8 12 15\n")
            f.write("CiudadA CiudadC 30 40 50 60\n")
        self.grafo.cargar_desde_archivo("logistica_test.txt")

    def test_cargar_ciudades(self):
        self.assertIn("CiudadA", self.grafo.ciudades)
        self.assertIn("CiudadC", self.grafo.ciudades)
        self.assertEqual(len(self.grafo.ciudades), 3)

    def test_matriz_clima_normal(self):
        matriz = self.grafo.obtener_matriz("normal")
        idx = self.grafo.indices
        self.assertEqual(matriz[idx["CiudadA"]][idx["CiudadB"]], 10)
        self.assertEqual(matriz[idx["CiudadB"]][idx["CiudadC"]], 5)

    def test_eliminar_arco(self):
        self.grafo.eliminar_arco("CiudadA", "CiudadB")
        matriz = self.grafo.obtener_matriz("normal")
        idx = self.grafo.indices
        self.assertEqual(matriz[idx["CiudadA"]][idx["CiudadB"]], math.inf)

    def test_floyd_y_centro(self):
        distancias, rutas = floyd_warshall(self.grafo, "normal")
        centro = calcular_centro(distancias, self.grafo.ciudades)
        self.assertEqual(centro, "CiudadA")

if __name__ == '__main__':
    unittest.main()
