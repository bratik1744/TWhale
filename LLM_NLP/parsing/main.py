import requests
import bs4


def razdel(s: str)-> (str, str):
    for i in range(len(s)):
        if s[i] == "—":
            return s[:i-1], s[i+2:]

'''
link = "https://empirix.ru/slovar-trejdera/"
f = open("termins.csv", "w", encoding="utf-8")
f.write("termins;definition;source\n")
soup = bs4.BeautifulSoup(requests.get(link).text, "html.parser")
for j in soup.find_all("p"):
    if "—" in j.text:
        a, b = razdel(j.text)
        if b[:5] == "тикер":
            break
        f.write(f"{a};{b};empirix.ru\n")
'''

'''
link = "https://fingramota.org/servisy/slovar"
soup = bs4.BeautifulSoup(requests.get(link).text, "html.parser")
lst_termins = []
lst_definition=[]
for j in soup.find_all("h4"):
    lst_termins.append(j.text)

for j in soup.find_all("p")[:-4]:
    lst_definition.append(j.text)

print(len(lst_termins), len(lst_definition))
for i in range(len(lst_termins)):
    f.write(f"{lst_termins[i]};{lst_definition[i]};fingramota.org")
'''
