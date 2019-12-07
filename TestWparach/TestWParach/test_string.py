#test_program.def
#imort modulu unittest():
import unittest

#import modulu (obiekt testowy()
import string_test

class TestProgram(unittest.TestCase):

    def test_add_1(self):
        wynik = string_test.add('ala','ma','kota')
        self.assertEqual(wynik, 'alamakota')

    def test_add_2(self):
        wynik = string_test.add('ala','ma')
        self.assertEqual(wynik, 'alama')

    def test_add_3(self):
        wynik = string_test.add('Kota','Ma')
        self.assertEqual(wynik, 'KotaMa')

    def test_add_4(self):
        wynik = string_test.add('','')
        self.assertEqual(wynik, '')

    def test_add_5(self):
        wynik = string_test.add('','','')
        self.assertEqual(wynik, '')


    def test_upper_1(self):
        wynik = string_test.upper('')
        self.assertEqual(wynik, '')

    def test_upper_2(self):
        wynik = string_test.upper('ala')
        self.assertEqual(wynik, 'ALA')

    def test_upper_3(self):
        wynik = string_test.upper('alaMAkOtA')
        self.assertEqual(wynik, 'ALAMAKOTA')

    def test_upper_4(self):
        wynik = string_test.upper('123456789')
        self.assertEqual(wynik, '123456789')

    def test_lower_1(self):
        wynik = string_test.lower('')
        self.assertEqual(wynik, '')

    def test_lower_2(self):
        wynik = string_test.lower('ALA')
        self.assertEqual(wynik, 'ala')

    def test_lower_3(self):
        wynik = string_test.lower('alaMAkOtA')
        self.assertEqual(wynik, 'alamakota')

    def test_lower_4(self):
        wynik = string_test.lower('123456789')
        self.assertEqual(wynik, '123456789')

    def test_len_1(self):
        wynik = string_test.length('')
        self.assertEqual(wynik, 0)

    def test_len_2(self):
        wynik = string_test.length('ALA')
        self.assertEqual(wynik, 3)

    def test_len_3(self):
        wynik = string_test.length('alaMAkOtA')
        self.assertEqual(wynik, 9)

    def test_len_4(self):
        wynik = string_test.length('123456789')
        self.assertEqual(wynik, 9)

    def test_islover_1(self):
        wynik = string_test.islover(1)
        self.assertEqual(wynik, False)

    def test_islover_2(self):
        wynik = string_test.islover('abcde')
        self.assertEqual(wynik, True)

    def test_islover_3(self):
        wynik = string_test.islover('')
        self.assertEqual(wynik, True)

    def test_islover_4(self):
        wynik = string_test.islover('asdfasdG')
        self.assertEqual(wynik, False)




if __name__ == '__main__':
    unittest.main()
