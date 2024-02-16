from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import json
import time

chrome_options = Options()
driver = webdriver.Chrome('Relu_Python_Task/chromedriver',chrome_options=chrome_options)

products = []

data = pd.read_csv('Amazon_Scraping.csv')
for asg in data.itertuples():
    id = asg.id
    country = asg.country
    asin = asg.Asin
    try:
        driver.get(f"https://www.amazon.{country}/dp/{asin}")
        Product_Title = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text
        Product_Image_URL = driver.find_element(By.XPATH, '//img[@id="landingImage"]').get_attribute('src')
        Price_of_the_Product = None
        price_xpaths = [
            '//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]/span[2]',
            '//span[@class="slot-price"]'
        ]
        for xpath in price_xpaths:
            try:
                Price_of_the_Product = driver.find_element(By.XPATH, xpath).text
                break
            except:
                pass
        Product_Details = driver.find_element(By.XPATH, '//div[@id="detailBulletsWrapper_feature_div"]').text
        print(id)
        print('Name',Product_Title)
        print('Imgurl',Product_Image_URL)
        print('price',Price_of_the_Product)
        print('Details', Product_Details)
        
        product_data = {"Product ID" : id,"Product Title": str(Product_Title),"Product Image URL": str(Product_Image_URL),"Price of the Product": str(Price_of_the_Product),"Product_Details": str(Product_Details)}
        products.append(product_data)
    except:
        pass

json_data = json.dumps(products, indent=4)
filepath = "Amazon_Scraping_Results.json"

with open(filepath, "w") as json_file:
    json_file.write(json_data)

print("JSON data exported to:", filepath)
driver.close()
