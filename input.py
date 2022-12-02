from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = Options()

options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)
options.add_argument("start-maximized")
# driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

link = 'https://www.facebook.com/marketplace/item/4428047700653795/?hoisted=false&ref=search&referral_code=null&referral_story_type=post&tracking=browse_serp%3A44626961-51c2-435a-bf01-4291ff93a140'
driver.get(link)

def ling_ceker():
    driver.get(link)
    try : 

        try:
            search = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/span/div/div/div/div/label/input')
        except:
            search = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/span/div/div/div/div/label/input')

        search.send_keys('\ue035')
        sleep(10)
        try:
            try:
                driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/h1/span')
                print('Titlenya Ada')
            except:                                    
                driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div[1]/h1/span')
                print('Titlenya Ada')
        except:
            print('Tittlenya Nggga Ada')
    except:
        print('input search tidak ada')

try:
    sleep(10)
    username = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input')
    password = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input')
    submit = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[3]/button')

    username.send_keys('teguhsaputra01@gmail.com')
    password.send_keys('NaiveBayes#1997')
    submit.submit()
    sleep(10)
    ling_ceker()
    sleep(1000)
except:
    ling_ceker()
    sleep(1000)
# driver.
# driver.re
# driver.navigate().to(driver.getCurrentUrl())

# driver.navigate().refresh()
# sleep(10)

# username = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
# password = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
# submit = driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]')

# username.send_keys('teguhsaputra01@gmail.com')
# password.send_keys('NaiveBayes#1997')
# submit.submit()
# sleep(1)

# notnow = driver.find_element(by=By.XPATH,value='/html/body/div[1]/section/main/div/div/div/div/button')
# notnow.click()
# sleep(1)
