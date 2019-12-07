import unittest
import programString

class TestTDD1(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(programString.upper("misiaczek"), "MISIACZEK")

    def test_firstUpper(self):
        self.assertEqual(programString.firstUpper("misiaczeK"), "Misiaczek")

    def test_length(self):
        self.assertEqual(programString.lengt("misiaczek"), 9)

    def test_lower(self):
        self.assertEqual(programString.lower("Kubus Puchatek"), "kubus puchatek")

    def test_replace(self):
        self.assertEqual(programString.replace("K", "j", "Kubus puchatek"), "jubus puchatek")

if __name__=='__main__':
    unittest.main()
