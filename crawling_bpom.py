from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import csv
import unittest

options = Options()
options.add_argument("start-maximized")

options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#link_open = open("url_link.txt","r")
#result = open("result.txt","a")

import unittest
import csv

class Test(unittest.TestCase):

    def test_read_csv_file(self):
       with open('DataBPOM.csv') as csvDataFile:
        csvReader = csv.DictReader(csvDataFile)
        myFile = open('ResultBPOM.csv','a',newline='')
        myHeader = ['STATUS','URL']
        writer = csv.DictWriter(myFile, fieldnames=myHeader)
        count = 0
        for row in csvReader:
            count += 1
            try:
                if "shopee" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.CLASS_NAME, value='VCNVHn')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '1','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Non-Active')
                elif "tokopedia" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.CLASS_NAME, value='css-1320e6c')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '1','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Non-Active')
                elif "bukalapak" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.CLASS_NAME, value='c-main-product__title')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '1','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Non-Active')
                elif "facebook" in row['URL']:
                    def check_title():
                        driver.get(row['URL'])
                        try : 
                            try:
                                search = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/span/div/div/div/div/label/input')
                                search.send_keys('\ue035')
                                print('Search X-Path 1')
                            except:
                                search = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div[1]/div/div/span/div/div/div/div/label/input')
                                search.send_keys('\ue035')
                                print('Search X-Path 2')
                            sleep(10)
                            try:
                                try:
                                    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/h1/span')
                                    myData = {'STATUS' : '2','URL' : row['URL']}
                                    writer.writerow(myData)
                                    print(count,'Active')
                                except:                                    
                                    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div[1]/h1/span')
                                    myData = {'STATUS' : '2','URL' : row['URL']}
                                    writer.writerow(myData)
                                    print(count,'Active')
                            except:
                                myData = {'STATUS' : '1','URL' : row['URL']}
                                writer.writerow(myData)
                                print(count,'Non-Active')
                        except:
                            print('key F5 doesnt work in facebook search marketplace')

                    driver.get(row['URL'])
                    try:
                        sleep(10)
                        username = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input')
                        password = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input')
                        submit = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[3]/button')

                        username.send_keys('teguhsaputra01@gmail.com')
                        password.send_keys('NaiveBayes#1997')
                        submit.submit()
                        sleep(10)
                        check_title()
                    except:
                        sleep(10)
                        check_title()
                elif "instagram" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/h2')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '0','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Ambigue')
                elif "linkedin" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/h1')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '0','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Ambigue')
                elif "kaskus" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.CLASS_NAME, value='item-name')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '1','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Non-Active')
                elif "twitter" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span[1]/span')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '0','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Ambigue')
                elif "blibli" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.CLASS_NAME, value='product-name')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '1','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Non-Active')
                elif "lazada" in row['URL']:
                    driver.get(row['URL'])
                    sleep(10)
                    try:
                        title = driver.find_element(by=By.CLASS_NAME, value='pdp-mod-product-badge-title')
                        myData = {'STATUS' : '2','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Active')
                    except:
                        myData = {'STATUS' : '1','URL' : row['URL']}
                        writer.writerow(myData)
                        print(count,'Non-Active')
                else:
                    driver.get(row['URL'])
                    sleep(10)
                    myData = {'STATUS' : '0','URL' : row['URL']}
                    writer.writerow(myData)
                    print(count,"Ambigue")
            except:
                myData = {'STATUS' : '1','URL' : row['URL']}
                writer.writerow(myData)
                print(count,"Broken Link")
                

if __name__ == "__main__":
    unittest.main()

