import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

class APregistration(unittest.TestCase):
    # warunki wstepne
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()

    def testTitle(self):
        driver=self.driver
        driver.find_element_by_class_name("login").click()
        driver.implicitly_wait(10)
        driver.find_element_by_id("email_create").send_keys("data@data.com")
        driver.find_element_by_id("SubmitCreate").click()
        driver.implicitly_wait(10)
        # WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(By.ID, "noSlide"))
        driver.find_element_by_id("id_gender2").click()
        driver.find_element_by_id("customer_firstname").send_keys("Basia")
        driver.find_element_by_id("customer_lastname").send_keys("Test")
        assert driver.find_element_by_id("email").get_attribute("value")=="data@data.com"
        driver.find_element_by_id("passwd").send_keys("Qwertry123")
        day = Select(driver.find_element_by_id("days"))
        day.select_by_value("16")
        month = Select(driver.find_element_by_id("months"))
        month.select_by_index("2")
        year = Select(driver.find_element_by_id("years"))
        year.select_by_value("1990")

        assert driver.find_element_by_id("firstname").get_attribute("value")=="Basia"
        assert driver.find_element_by_id("lastname").get_attribute("value")=="Test"

        driver.find_element_by_id("address1").send_keys("adres")
        driver.find_element_by_id("city").send_keys("Katowice")
        driver.find_element_by_id("postcode").send_keys("00000")
        driver.find_element_by_id("phone_mobile").send_keys("123456789")
        driver.find_element_by_id("alias").send_keys("moj adres")
        driver.find_element_by_id("submitAccount").click()

        errors = driver.find_elements_by_xpath('//div[@class="alert alert-danger"]/ol/li')
        assert len(errors)==1
        assert "This country" in errors[0].text


    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=0)
