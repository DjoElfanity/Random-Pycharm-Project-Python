import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from faker import Faker

def generate_random_name():
    fake = Faker()
    return fake.name()

random_names = generate_random_name()
random_prenom = random_names[0]
random_name = random_names[1]
username= "gcd"
password = "acial!gcd2018"
montant_achat = random.randint(5000, 48000)
pourcentage = random.randint(80,100)
duree  = random.randint(12,48)
categorie  = random.randint(0,1)
montant_credit =  (montant_achat * pourcentage) / 100

driver = webdriver.Chrome()
driver.get("http://credit-auto.qsiconseil.ma/")
bouton_acces = driver.find_element(By.XPATH, '//*[@id="lnkAccesCreditAuto"]').click()
userfield = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)  # 00
time.sleep(1)
passfield = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)  # 01
time.sleep(1)
connection_button = driver.find_element(By.XPATH, '//*[@id="page-top"]/div[2]/div/div/form/fieldset/button').click()

simulation_contrat_link = driver.find_element(By.XPATH , '//*[@id="lnkSimulation"]').click()
time.sleep(3)

input_achat = driver.find_element(By.XPATH , '//*[@id="form_simulation_montantAchat"]').send_keys(montant_achat)
time.sleep(1)
input_credit = driver.find_element(By.XPATH , '//*[@id="form_simulation_montantCredit"]').send_keys(montant_credit)
time.sleep(1)
input_duree = driver.find_element(By.XPATH ,'//*[@id="form_simulation_duree"]').send_keys(duree)
time.sleep(1)
input_categorie = driver.find_element(By.XPATH , '//*[@id="form_simulation_categorie"]').click()
time.sleep(1)
if categorie == 0 :
    categorie_A = driver.find_element(By.XPATH , '//*[@id="form_simulation_categorie"]/option[1]').click()
    time.sleep(1)
else :
    categorie_B = driver.find_element(By.XPATH, '//*[@id="form_simulation_categorie"]/option[2]').click()
    time.sleep(1)

calculer_credit = driver.find_element(By.XPATH , '//*[@id="calcul"]').click()
time.sleep(3)
creer_contrat = driver.find_element(By.XPATH ,'//*[@id="lnkCreerContrat"]').click()

#Formuliare AJOUT CLIENT