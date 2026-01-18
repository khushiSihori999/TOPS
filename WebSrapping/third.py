from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import pymysql


conn=pymysql.connect(

    host="localhost",
    user="root",
    password="",
    database="webscrapping"
)

cursor=conn.cursor()

edge_options=Options()
service=Service("msedgedriver.exe")

driver=webdriver.Edge(service=service,options=edge_options)
driver.get("https://quotes.toscrape.com/")

time.sleep(2)

quotes=driver.find_elements(By.CLASS_NAME,"text")

for q in quotes:
    sql="INSERT INTO salesquotes(quote) VALUES (%s)"
    cursor.execute(sql,(q.text,))

conn.commit()

driver.quit()
cursor.close()
conn.close()

print("Qutes successfully stored in Mysql database")

