import unittest
import math
from calculator import add, subtract, multiply, divide, power, sqrt

class TestCalculadora(unittest.TestCase):
    
    # Testes para soma
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(-1, -1), -2)

    # Testes para subtração
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(1.5, 0.5), 1.0)

    # Testes para multiplicação
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1.5, 2), 3.0)
        self.assertEqual(multiply(-1.5, -2), 3.0)

    # Testes para divisão
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, 0), "Erro: Divisão por zero não é permitida.")  # Divisão por zero
        self.assertEqual(divide(5.0, 2.0), 2.5)

    # Testes para potência
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(4, -1), 0.25)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(2, 0.5), math.sqrt(2))  # Teste de raiz com potência

    # Testes para raiz quadrada
    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(-1), "Erro: Raiz quadrada de número negativo não é permitida.")  # Raiz negativa
        self.assertEqual(sqrt(2), math.sqrt(2))

if __name__ == '__main__':
    unittest.main()
