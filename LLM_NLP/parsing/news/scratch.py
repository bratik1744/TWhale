import csv
import requests
import bs4
from tqdm import tqdm

def pars(url: str) -> (str, str):
    soup = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
    body = ""
    for i in soup.find("div", attrs={"class": "topic bluid_41471"}).find_next("div", attrs={"class": "content"}):
        if any([j.isalpha() for j in i.text]):
            #print(i.text.replace("\n", ""))
            body += i.text.replace("\n", "").replace("\r", "") + " "
            #print("__________")
    ref = soup.find("div", attrs={"class": "topic bluid_41471"}).find_next("div", attrs={"class": "content"}).a["href"]
    return body, ref




with open("smart_lab/news_smart_lab_hrefs.csv", "r", encoding="utf-8") as f:
    file_reader = csv.DictReader(f)
    lst = []
    for i in tqdm(file_reader):
        body, ref = pars(i["href"])
        i["body"] = body
        i["ref"] = ref
        lst.append(i)


print(lst)
with open("news_smart.csv", "w", encoding="utf-8", newline='') as f:
    names = ["id", "date", "title", "href", "body", "ref"]
    file_writer = csv.DictWriter(f, delimiter = ",", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerows(lst)

