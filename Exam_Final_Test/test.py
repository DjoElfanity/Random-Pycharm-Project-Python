from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import HtmlTestRunner

import time
import unittest


class GoogleSearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://credit-auto.qsiconseil.ma/")

    def tearDown(self):
        self.driver.quit()

    def authenticate(self):
        boutique = self.driver.find_element(By.ID, "lnkAccesCreditAuto")
        boutique.click()
        field1 = self.driver.find_element(By.ID, "username")
        field2 = self.driver.find_element(By.ID, "password")
        button = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/div[2]/div/div/form/fieldset/button')

        field1.send_keys("gcd")
        field2.send_keys("acial!gcd2018")

        try:
            button.click()
        except Exception:
            print(Exception)

    def test_CreditAuto(self):
        self.authenticate()

        assert self.driver.find_element(By.XPATH, '/html/body/div[2]/div/pre/b[1]').text == "gcd"

        contract = self.driver.find_element(By.XPATH, '/html/body/nav/div/div[1]/ul/li[2]/a')
        contract.click()
        self.driver.find_element(By.ID, "lnkCreerContrat").click()

        m_achat = self.driver.find_element(By.ID, "form_simulation_montantAchat")
        m_credit = self.driver.find_element(By.ID, "form_simulation_montantCredit")
        duree = self.driver.find_element(By.ID, "form_simulation_duree")
        categ = self.driver.find_element(By.ID, "form_simulation_categorie")

        # Must be above 5000
        m_achat.send_keys(5000)

        # This too
        m_credit.send_keys(5000)

        # Entre 12 et 48

        duree.send_keys(20)

        categ.click()
        select = Select(categ)
        select.select_by_value("B")

        self.driver.find_element(By.ID, "calcul").click()

        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/div[1]/a[2]").click()

        self.driver.find_element(By.ID, "name").send_keys("Elfanity")
        self.driver.find_element(By.ID, "firstname").send_keys("Jad")
        self.driver.find_element(By.ID, "btnRecherchAer").click()

        assert self.driver.find_element(By.ID, "divErrorMessage")

        self.driver.find_element(By.ID, "compte").send_keys("123456789101")
        self.driver.find_element(By.ID, "solde").send_keys("12000")
        self.driver.find_element(By.ID, "nom").send_keys("Elfanity")
        self.driver.find_element(By.ID, "prenom").send_keys("Jad")
        self.driver.find_element(By.ID, "age").send_keys("21")

        self.driver.find_element(By.ID, "addresse").send_keys("Bourgogne")
        self.driver.find_element(By.ID, "postal").send_keys("20800")
        self.driver.find_element(By.ID, "city").send_keys("Casablanca")

        self.driver.find_element(By.ID, "add").click()
        time.sleep(5)

        try:
            self.driver.find_element(By.ID, "mnAccueil").click()
        except Exception:
            print("fin")


if __name__ == "__main__":
    unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="report"))