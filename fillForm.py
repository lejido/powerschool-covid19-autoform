import time

import os

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By

def noSymptoms(driver):  
  load_dotenv() 

  time.sleep(10) 
  
  # Symptoms 
  driver.find_element(By.XPATH, '//*[@id="c1756072-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756048-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756039-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756045-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756036-1"]').click()
  driver.find_element(By.XPATH, '//*[@id="c1756078-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756042-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756069-1"]').click()
  driver.find_element(By.XPATH, '//*[@id="c1756084-1"]').click()
  driver.find_element(By.XPATH, '//*[@id="c1756081-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756057-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756054-1"]').click()
  driver.find_element(By.XPATH, '//*[@id="c1756060-1"]').click()
  driver.find_element(By.XPATH, '//*[@id="c1756030-1"]').click()
  driver.find_element(By.XPATH, '//*[@id="c1756075-1"]').click()
  
  # please verify 
  driver.find_element(By.XPATH, '//*[@id="c1756066-1"]').click()
  driver.find_element(By.XPATH, '//*[@id="c1756063-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756027-1"]').click() 

  # summary 
  driver.find_element(By.XPATH, '//*[@id="c5845590-1"]').click() 
  driver.find_element(By.XPATH, '//*[@id="c1756051-1"]').click() 

  # consent 
  consent_name = os.environ.get('CONSENT_NAME')
  driver.find_element(By.XPATH, '//*[@id="c1756017-0"]').click() 
  driver.find_element(By.XPATH, '//*[@id="tb1756033-0"]').send_keys(consent_name)

  # submit 
  driver.find_element(By.XPATH, '//*[@id="submitButton"]').click() 
  time.sleep(10)
  driver.quit() 
