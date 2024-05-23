import unittest

# Función a probar
def sumar(a, b):
    return a + b

# Clase de pruebas unitarias
class TestSumar(unittest.TestCase):

    # Prueba: Suma de números positivos
    def test_suma_numeros_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    # Prueba: Suma de números negativos
    def test_suma_numeros_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)

    # Prueba: Suma de un número positivo y un número negativo
    def test_suma_positivo_y_negativo(self):
        self.assertEqual(sumar(2, -3), -1)

# Ejecutar las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
