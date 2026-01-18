from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time


edge_options=Options()
edge_options.add_argument("--start -maximized")

service=Service("msedgedriver.exe")

driver=webdriver.Edge(service=service,options=edge_options)

driver.get("http://www.flipkart.com")
time.sleep(5)

driver.quit()