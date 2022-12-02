from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import csv

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#link_open = open("url_link.txt","r")
#result = open("result.txt","a")

#all_links = link_open.read()
# print(all_links)
#all_links.strip()
#arr = all_links.split(',')

#for i in range(len(arr)):
#    arr[i]=arr[i].replace('\n','')

#count = 0

#for x in arr:
    #count += 1
    try:
        if "shopee" in x:
            driver.get(x)
            print("shopee")
                #sleep(1)
                #price = driver.find_element(by=By.CLASS_NAME, value='VCNVHn')
                #result.write('Active\n')
                #print(f'{count} Active')
        elif "tokopedia" in x:
            driver.get(x)
            print("tokopedia")
        elif "bukalapak" in x:
            driver.get(x)
            print("bukalapak")
        elif "facebook" in x:
            driver.get(x)
            print("facebook")
        elif "instagram" in x:
            driver.get(x)
            print("instagram")
        elif "linkedin" in x:
            driver.get(x)
            print("linkedin")
        elif "kaskus" in x:
            driver.get(x)
            print("kaskus")
        elif "twitter" in x:
            driver.get(x)
            print("twitter")
        elif "blibli" in x:
            driver.get(x)
            print("blibli")
        elif "lazada" in x:
            driver.get(x)
            print("lazada")
        else:
            driver.get(x)
            print("from another web")
            
    except:
        #result.write('Non-Active\n')
        #print(f'{count} Non-Active')
        print("link error")
result.close()
link_open.close()

#driver.get("https://shopee.co.id/Sarian-skincare-i.29415595.7717018829")
#driver.get("https://shopee.co.id/vitamin-mata-tarax-i.300321748.5348658060")


#try:
#    price = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[3]/div/div[1]')
#    print('title exist')
#except:
#    print('title doesnt exist')
#
#driver.close()
