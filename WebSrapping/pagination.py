
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

service=Service("msedgedriver.exe")

options=webdriver.EdgeOptions()
options.add_argument("--start -maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver=webdriver.Edge(service=service, options=options)
wait=WebDriverWait(driver,20)

# wait until  product load
driver.get("https://www.meesho.com/search?q=kurti")

#scroll multiple times
for _ in range(8):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)

#select product cards
products=driver.find_elements(By.XPATH, "//a[contains(@href,'/product')]")

print("product found:" ,len (products))

data= []

for p in products:
    try:
        name=p.find_element(By.XPATH, ".//p").text
    except:
        name=""

    try:
        price=p.find_element(By.XPATH,".//h5").text
    except:
        price=""

    try:
        img=p.find_element(By.TAG_NAME,"img").get_attribute("src")

    except:
        img=""

    link=p.get_attribute("href")

    if name and price:
        data.append([name,price,img,link])

driver.quit()

#save csv

with open("meesho_products.csv","w",newline="",encoding="utf-8") as f:

    writer=csv.writer(f)
    writer.writerow(["Name","Price","Image","Link"])
    writer.writerows(data)

print("csv saved with", len(data),"products")
