import unittest
import mojprogam

class TestTDD(unittest.TestCase):
    def test_zwroc_100(self):
        wynik=mojprogam.zwroc_100()
        self.assertEqual(wynik, 100)

    def test_zwroc_parametr(self):
        self.assertEqual(mojprogam.zwroc_parametr(124), 124)

    def test_dodaj_2_2(self):
        self.assertEqual(mojprogam.dodaj(2,2), 4)

    def test_dodaj_8_15(self):
        self.assertEqual(mojprogam.dodaj(8,15), 23)

    def test_mnozenie_7_8(self):
        self.assertEqual(mojprogam.mnozenie(7, 8), 56)

    def test_hello_world(self):
        self.assertEqual(mojprogam.hello_world("Hello World"), "Hello World")

    def test_odejmij_8_2(self):
        self.assertEqual(mojprogam.odejmij(8,2), 6)

    def test_pierwiastek_81(self):
        self.assertEqual(mojprogam.pierwiastek(81), 9)

    def test_potega2_3(self):
        self.assertEqual(mojprogam.potega(2, 3), 8)

if __name__=='__main__':
    unittest.main()
