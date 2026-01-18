
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

edge_options=Options()
service=Service("msedgedriver.exe")

driver=webdriver.Edge(service=service,options=edge_options)
driver.get("https://quotes.toscrape.com/")

time.sleep(10)

quotes=driver.find_elements(By.CLASS_NAME,"text")

print("Quotes:\n")

for q in quotes:
    print(q.text)

driver.quit()