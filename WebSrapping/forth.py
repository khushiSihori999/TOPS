

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import csv

edge_options=Options()
service=Service("msedgedriver.exe")

driver=webdriver.Edge(service=service,options=edge_options)
driver.get("https://quotes.toscrape.com/")

time.sleep(2)

quotes=driver.find_elements(By.CLASS_NAME,"text")

with open("quotes.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["Quote"])

    for q in quotes:
        writer.writerow([q.text])

driver.quit()