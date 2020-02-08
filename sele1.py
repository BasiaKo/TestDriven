import unittest
from selenium import webdriver
from time import sleep

#przypadek testowy
class WsbPlChceck(unittest.TestCase):
    # warunki wstepne
    def setUp(self):
        # print("jestem setUp")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.wsb.pl")
        self.driver.maximize_window()

    def testTitle(self):
        self.assertIn("Bankowe", self.driver.title)
        sleep(5)


    # prawdziwy test
    def testPierwszy(self):
        assert 2==2

    def testDrugi(self):
        assert 3==3

    def tearDown(self):
        # print("Sprzatanie po kazdym tescie")
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=0)
