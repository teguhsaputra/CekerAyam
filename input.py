from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get('https://www.instagram.com/sbsshopbali')

sleep(1)

username = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
password = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
submit = driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]')

username.send_keys('teguhsaputra01@gmail.com')
password.send_keys('NaiveBayes#1997')
submit.submit()
sleep(1)

notnow = driver.find_element(by=By.XPATH,value='/html/body/div[1]/section/main/div/div/div/div/button')
notnow.click()
sleep(1)
