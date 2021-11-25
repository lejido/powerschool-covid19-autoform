import os 

from fillForm import noSymptoms

from dotenv import load_dotenv 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('/usr/local/bin/chromedriver') 

chrome_options = Options()
#chrome_options.add_argument("--headless") # uncomment line to remove visual aspect 

driver = webdriver.Chrome(service=s, options=chrome_options) 
driver.get('https://ps001.bergen.org/public/')

load_dotenv()

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD') 

driver.find_element(By.ID, 'fieldAccount').send_keys(username) 
driver.find_element(By.ID, 'fieldPassword').send_keys(password) 
driver.find_element(By.ID, 'btn-enter-sign-in').click() 

driver.get('https://ps001.bergen.org/guardian/form.html?formid=1756009')

noSymptoms(driver)

print("DONE")







