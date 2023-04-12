import time
from selenium import webdriver
from selenium.webdriver.common.by import By

data = [
    ['rcd', 'acial!rcd2018'],
    ['lcd', 'acial!acd2018'],
    ['gcd', 'acial!gcd2018'],
    ['acd', 'acial!acd2018'],
]

driver = webdriver.Chrome()
driver.get("http://credit-auto.qsiconseil.ma/")
bouton_acces = driver.find_element(By.XPATH, '//*[@id="lnkAccesCreditAuto"]').click()


for i in range(len(data)):
    userfield = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(data[i][0])  # 00
    time.sleep(1)
    passfield = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(data[i][1])  #01
    time.sleep(1)
    connection_button = driver.find_element(By.XPATH, '//*[@id="page-top"]/div[2]/div/div/form/fieldset/button').click()
    time.sleep(1)
    deco = driver.find_element(By.XPATH , '/html/body/nav/div/div[3]/a')
    bouton_acces = driver.find_element(By.XPATH, '//*[@id="lnkAccesCreditAuto"]').click()

    clear_input = driver.find_element(By.XPATH, '//*[@id="username"]').clear()
    clear_pswd = driver.find_element(By.XPATH, '//*[@id="password"]').clear()
    time.sleep(1)