from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image 
import pytesseract
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import time

chrome_options = Options()
driver = webdriver.Chrome('Relu_Python_Task/chromedriver',chrome_options=chrome_options)
driver.get('https://www.amazon.com/errors/validateCaptcha')
while True:
    try:
        captcha = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img').get_attribute('src')
    
        data = urllib.request.urlretrieve(captcha,"captcha.jpg")
    
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
         
        img = Image.open('captcha.jpg')
    
        text = pytesseract.image_to_string(img)
        
        captcha_box = driver.find_element(By.XPATH,'//*[@id="captchacharacters"]')
        captcha_box.send_keys(text)
        captcha_box = driver.find_element(By.XPATH,'/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button')
        captcha_box.click()
        time.sleep(1)
    except:
        time.sleep(1)
driver.close()
