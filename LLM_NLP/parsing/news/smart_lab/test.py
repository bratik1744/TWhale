import csv
from tqdm import tqdm



with open("news_smart.csv", "r", encoding="utf-8") as f:
    file_reader = csv.DictReader(f)
    lst = []
    a = 0
    for i in tqdm(file_reader):
        if i["body"] and i["ref"]:
            continue
        a += 1
    print(a)