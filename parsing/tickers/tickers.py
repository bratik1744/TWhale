from tqdm import tqdm
from selenium import webdriver
import time
import bs4

t = open("MOEX_tickers.csv", "r", encoding='utf-8')
lst = [i.split(";")[0] for i in t.readlines()]
print(lst)
t.close()
f = open("tickers.csv", "w", encoding="utf-8")
driver = webdriver.Chrome()
for i in tqdm(lst):
    url = f'https://bcs.ru/markets/{i}/tqbr'
    try:
        driver.get(url)
        time.sleep(5)
        html_code = driver.page_source
        soup = bs4.BeautifulSoup(html_code, "html.parser")
        write = i + "#"
        write += soup.find_all("span", attrs={"class": "tsW0e"})[-1].text + "#"
        for i in soup.find("div", attrs={"class": "zps7U"}).div:
            write += i.text.replace("\n", " ")
        f.write(write + "\n")
    except BaseException:
        print(f"не найден тикер {i}")


