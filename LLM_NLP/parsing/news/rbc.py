from tqdm import tqdm
from selenium import webdriver
import time
import bs4

url = "https://quote.rbc.ru/tag/stocks"
driver = webdriver.Chrome()
driver.get(url)
stat = time.time()
while True:
    while time.time() - stat < 1200:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    a = input("sfkkfs")
    if a:
        break

code = driver.page_source

f = open("rbc.txt", "w", encoding="utf-8")
f.write(code)
