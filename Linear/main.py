import time


from selenium import webdriver
from selenium.webdriver.common.by import By
import sys


def calcul(path,number):
    for i in number:
        driver.find_element(By.XPATH, path).send_keys(i)
number = "2222222222222222"

#Instancier
driver = webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/")
#weather = driver.find_element(By.XPATH , "//*[@id='temperature']").text
weather = "34 °C "
x= 33


def findPrice(object):
    x = []
    var = driver.find_elements(By.XPATH, f"//p[contains(.,'{object}')]/following-sibling::p")
    for i in var:
        print(i.text.split()[-1])  ## 140 / 121 / 160
        x.append(i.text.split()[-1])
    x.sort()
    print(f"La valeur minimal de {object} est {x[0]}")  ## 121

    for i in var:
        if (x[0] == i.text.split()[-1]):
                driver.find_element(By.XPATH, f"//p[contains(.,'{object}')]/following-sibling::button").click()
if(weather >= "34 °C"):

    input1 = driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/a/button")
    input1.click()
    findPrice("SPF-30")
    findPrice("SPF-50")

    input2 = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[3]/button")
    input2.click()
    input3 = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/button")
    input3.click()
    input4 = driver.find_element(By.XPATH ,"/html/body/nav/ul/button")
    input4.click()
    valider = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/button").click()
    driver.switch_to.frame("stripe_checkout_app")
    email = driver.find_element(By.XPATH ,"//*[@id='email']").send_keys('j.el_fanity@mundiapolis.ma')
    numero_carte = calcul("//*[@id='card_number']",number)
    date = calcul("//*[@id='cc-exp']","1022")
    cvv = driver.find_element(By.XPATH,"//*[@id='cc-csc']").send_keys("000")
    cliqued = driver.find_element(By.XPATH, "//*[@id='submitButton']/span/span").click()
    ##zip = driver.find_element(By.XPATH, "//*[@id='billing-zip']").send_keys("02108")




elif(weather <= "19 °C"):
    print("Non")























